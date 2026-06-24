from collections import namedtuple
from typing import Any

import abjad

from ..utils import load_config


def _nullify_list(property: list[Any], default_value: Any = None) -> list[Any]:
    r"""
    Creates list with the same structure as an input list. Used to take the staff_names property
        from config.toml and create a similar structure with default_values for missing properties.

    Args:
        property (list[Any]): Reference list to be nullified.
        default_value (Any): Default value in the output list, defaults to ``None``.

    Returns:
        list[Any]: Output list with identical structure to input ``property`` but with nullified
            values.

    Example:
        >>> staff_names = [
        ...     "Flute",
        ...     ["Piano_Upper", "Piano_Middle", "Piano_Lower"],
        ...     ["Harp_Upper", "Harp_Lower"],
        ...     "Cello",
        ... ]
        >>> _nullify_list(staff_names)
        [
            None,
            [None, None, None],
            [None, None],
            None,
        ]
    """
    output_list = []
    for value in property:
        output_list.append(default_value if not isinstance(value, list) else _nullify_list(value))
    return output_list


def create_staves() -> tuple[list[abjad.Staff], list[namedtuple]]:
    r"""
    Creates list of staves and list of instrument properties (staves, instrument names, clefs,
        etc.).

    Args:
        None

    Returns:
        tuple[list[abjad.Staff], list[namedtuple]]: A ``tuple`` with two elements, 1) all staves
            (as ``list`` of ``abjad.Staff``'s) and 2) all instrument propertuies (as a ``list`` of
            ``namedtuple``'s).
    """
    # reading config.toml file
    config_dict = load_config()

    STAFF_NAMES = config_dict["instrumentation"]["staff_names"]
    CONTEXTS = config_dict["instrumentation"]["contexts"]
    INSTRUMENT_NAMES = config_dict["instrumentation"]["instrument_names"]
    SHORT_INSTRUMENT_NAMES = config_dict["instrumentation"]["short_instrument_names"]
    try:
        INITIAL_CLEFS = config_dict["instrumentation"]["initial_clefs"]
    except KeyError:
        INITIAL_CLEFS = _nullify_list(STAFF_NAMES, None)

    # Defining named tuple
    InstrumentProperties = namedtuple(
        "Staff",
        [
            "container",
            "instrument_name",
            "short_instrument_name",
            "initial_clef",
            "context",
        ],
    )

    # creating staves and instrument_properties
    staves = []
    instrument_properties = []

    for index, staff_name in enumerate(STAFF_NAMES):
        # single staff instruments, i.e. not in a StaffGroup
        if not isinstance(staff_name, list):
            staff = abjad.Staff(name=staff_name)
            instrument_property = InstrumentProperties(
                container=staff,
                instrument_name=INSTRUMENT_NAMES[index],
                short_instrument_name=SHORT_INSTRUMENT_NAMES[index],
                initial_clef=INITIAL_CLEFS[index],
                context=CONTEXTS[index],
            )
            staves.append(staff)
            instrument_properties.append(instrument_property)
        else:
            # instruments in a StaffGroup
            staff_group = abjad.StaffGroup(
                name=INSTRUMENT_NAMES[index],
                lilypond_type=CONTEXTS[index],
            )
            for single_name in staff_name:
                staff = abjad.Staff(name=single_name)
                staves.append(staff)
                staff_group.append(staff)
            instrument_property = InstrumentProperties(
                container=staff_group,
                instrument_name=INSTRUMENT_NAMES[index],
                short_instrument_name=SHORT_INSTRUMENT_NAMES[index],
                initial_clef=INITIAL_CLEFS[index],
                context=CONTEXTS[index],
            )
            instrument_properties.append(instrument_property)

    return staves, instrument_properties
