import random
from typing import Optional

import abjad


def make_material_C(
    seed: Optional[int] = None,
) -> list[abjad.Staff]:
    r"""
    Generates material for Segment C

    Args:
        seed: optional ``int`` for random seed.

    Returns:
        ``list`` of ``abjad.Staff``.
    """
    if seed is not None:
        random.seed(seed)

    material_C = [
        abjad.Staff([abjad.Note(random.randint(24, 36), (1, 4)) for _ in range(6)]),
        abjad.Staff([abjad.Note(random.randint(24, 36), (1, 4)) for _ in range(6)]),
        abjad.Staff([abjad.Note(random.randint(12, 24), (1, 2)) for _ in range(3)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(3)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (3, 2)) for _ in range(1)]),
        abjad.Staff([abjad.Note(random.randint(-24, -12), (1, 2)) for _ in range(3)]),
        abjad.Staff([abjad.Note(random.randint(-24, -12), (3, 2)) for _ in range(1)]),
    ]

    return material_C