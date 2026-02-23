import random

import abjad

from .material_C_definitions import RANDOM_SEED


def make_material_C() -> list[abjad.Staff]:
    r"""
    Generates material for Segment C

    Args:
        None

    Returns:
        ``list`` of ``abjad.Staff``.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

    material_C = [
        abjad.Staff([abjad.Note(random.randint(24, 36), (1, 4)) for _ in range(6)]),
        abjad.Staff([abjad.Note(random.randint(24, 36), (1, 4)) for _ in range(6)]),
        abjad.Staff([abjad.Rest("r4") for _ in range(6)]),
        abjad.Staff([abjad.Rest("r4") for _ in range(6)]),
        abjad.Staff([abjad.Note(random.randint(0, 12), (3, 2)) for _ in range(1)]),
        abjad.Staff([abjad.Note(random.randint(-24, -12), (1, 2)) for _ in range(3)]),
        abjad.Staff([abjad.Note(random.randint(-24, -12), (3, 2)) for _ in range(1)]),
    ]

    return material_C
