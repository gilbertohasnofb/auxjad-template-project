import random

import abjad
import auxjad

from .segment_02_definitions import (
    INCLUDE_DOUBLE_BARLINE,
    OUTPUT_N,
    RANDOM_SEED,
    SEGMENT_MATERIAL,
    STEP_SIZE,
    WINDOW_SIZE,
)
from .. import tools


def make_segment_02(
    materials_dict: dict[str, abjad.Container],
) -> list[abjad.Selection]:
    r"""
    Makes segment #02.

    Args:
        materials_dict: ``dict`` with all materials organised by key, value pairs, with keys as
            ``str`` representing the name of the material and values as ``abjad.Container``
            containing the respective material's music.

    Returns:
        ``list`` of ``abjad.Selection``'s.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

    segment_02_music = []
    for staff_material in materials_dict[SEGMENT_MATERIAL]:
        looper = auxjad.WindowLooper(
            staff_material,
            window_size=WINDOW_SIZE,
            step_size=STEP_SIZE,
        )
        staff_music = looper.output_n(OUTPUT_N)
        if INCLUDE_DOUBLE_BARLINE:
            abjad.attach(
                abjad.BarLine("||"),
                abjad.select(staff_music).leaf(-1),
            )
        segment_02_music.append(staff_music)

    return segment_02_music
