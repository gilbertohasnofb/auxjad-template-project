import random
from typing import Optional

import abjad


def make_material_B(
    seed: Optional[int] = None,
) -> list[abjad.Staff]:
    r"""
    Generates material for Segment B

    Args:
        seed: optional ``int`` for random seed.

    Returns:
        ``list`` of ``abjad.Staff``.
    """
    if seed is not None:
        random.seed(seed)

    material_B = [
        abjad.Staff([abjad.Note(random.randint(12, 36), (1, 16)) for _ in range(12)]),
        abjad.Staff([abjad.Note(random.randint(12, 36), (1, 16)) for _ in range(12)]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Note(random.randint(-24, 0), (1, 8)) for _ in range(6)]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Rest((3, 4))]),
    ]

    return material_B
