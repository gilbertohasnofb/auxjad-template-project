import random
from typing import Optional

import abjad
import auxjad
from tqdm import tqdm

from .. import materials
from .. import tools


def make_segment_C(
    *,
    window_size: abjad.Duration,
    step_size: abjad.Duration,
    seed: Optional[int] = None,
) -> tuple[abjad.Staff]:
    r"""
    Makes segment C.

    Args:
        window_size: ``abjad.Duration`` with the length of the window size of the ``WindowLooper``.
        step_size: ``abjad.Duration`` with the step size of the ``WindowLooper``.
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

    material_C_staves = materials.make_material_C(seed=seed)

    segment_C_music = []
    for staff in material_C_staves:
        looper = auxjad.WindowLooper(
            staff,
            window_size=window_size,
            step_size=step_size,
        )
        segment_C_music.append(looper.output_all())

    return segment_C_music
