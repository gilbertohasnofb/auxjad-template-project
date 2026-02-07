from collections import namedtuple

import abjad
import tomli


def create_staves() -> tuple[list[abjad.Staff], list[namedtuple]]:
    r"""
    Creates list of staves and list of instrument properties (staves, instrument names, clefs,
        etc.).

    Args:
        None

    Returns:
        ``Tuple`` containing ``list`` of ``abjad.Staff``'s and ``list`` of ``namedtuple``'s.
    """
    # reading config.toml file
    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    STAFF_NAMES = config_dict["instrumentation"]["staff_names"]
    CONTEXTS = config_dict["instrumentation"]["contexts"]
    INSTRUMENT_NAMES = config_dict["instrumentation"]["instrument_names"]
    SHORT_INSTRUMENT_NAMES = config_dict["instrumentation"]["short_instrument_names"]
    INITIAL_CLEFS = config_dict["instrumentation"]["initial_clefs"]

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
