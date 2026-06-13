import random

import abjad
import auxjad

from .. import tools  # noqa: F401
from .segment_01_definitions import (
    INCLUDE_DOUBLE_BARLINE,
    RANDOM_SEED,
    SEGMENT_MATERIAL,
    STEP_SIZE,
    WINDOW_SIZE,
)


def make_segment_01(
    materials_dict: dict[str, abjad.Container],
) -> list[abjad.Staff]:
    r"""
    Makes Segment #01.

    Args:
        materials_dict (dict): All materials organised by key, value pairs, with keys as ``str``
            representing the name of the material and values as ``abjad.Container`` containing the
            respective material's music.

    Returns:
        list[abjad.Staff]: list of staves for the full segment.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

    output_staves = []
    for staff_material in materials_dict[SEGMENT_MATERIAL]:
        looper = auxjad.WindowLooper(
            staff_material,
            window_size=WINDOW_SIZE,
            step_size=STEP_SIZE,
        )
        staff_music = looper.output_all()
        if INCLUDE_DOUBLE_BARLINE:
            abjad.attach(
                abjad.BarLine("||"),
                abjad.select(staff_music).leaf(-1),
            )
        output_staves.append(staff_music)

    return output_staves
