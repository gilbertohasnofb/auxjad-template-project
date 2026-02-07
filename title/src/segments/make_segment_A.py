import random
from typing import Optional

import abjad
import auxjad
from tqdm import tqdm

from .. import materials
from .. import tools


def make_segment_A(
    *,
    window_size: abjad.Duration,
    step_size: abjad.Duration,
    include_double_barline: bool,
    seed: Optional[int] = None,
) -> tuple[abjad.Staff]:
    r"""
    Makes segment A.

    Args:
        window_size: ``abjad.Duration`` with the length of the window size of the ``WindowLooper``.
        step_size: ``abjad.Duration`` with the step size of the ``WindowLooper``.
        include_double_barline: if ``True``, double bar lines are added at the end of the segment.
        seed: optional ``int`` for random seed.

    Returns:
        ``tuple`` of ``abjad.Staff``'s.
    """
    if seed:
        random.seed(seed)

    if not isinstance(window_size, abjad.Duration):
        window_size = abjad.Duration(window_size)

    if not isinstance(step_size, abjad.Duration):
        step_size = abjad.Duration(step_size)

    material_A_staves = materials.make_material_A(seed=seed)

    segment_A_music = []
    for staff in material_A_staves:
        looper = auxjad.WindowLooper(
            staff,
            window_size=window_size,
            step_size=step_size,
        )
        staff_music = looper.output_all()
        if include_double_barline:
            abjad.attach(
                abjad.BarLine("||"),
                abjad.select(staff_music).leaf(-1),
            )
        segment_A_music.append(staff_music)

    return segment_A_music
