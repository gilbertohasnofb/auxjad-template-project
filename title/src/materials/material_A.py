import random
from typing import Optional

import abjad


def make_material_A(
    seed: Optional[int] = None,
) -> list[abjad.Staff]:
    r"""
    Generates material for Segment A

    Args:
        seed: optional ``int`` for random seed.

    Returns:
        ``list`` of ``abjad.Staff``.
    """
    if seed is not None:
        random.seed(seed)

    material_A = [
        abjad.Staff([abjad.Note(random.randint(12, 24), (1, 4)) for _ in range(4)]),
        abjad.Staff([abjad.Note(random.randint(12, 24), (1, 4)) for _ in range(4)]),
        abjad.Staff([abjad.Note(random.randint(0, 12), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(0, 12), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
    ]

    return material_A
