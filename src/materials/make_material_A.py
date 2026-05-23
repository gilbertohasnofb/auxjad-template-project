import random

import abjad

from .material_A_definitions import RANDOM_SEED


def make_material_A() -> list[abjad.Staff]:
    r"""
    Generates material for Segment A

    Args:
        None

    Returns:
        ``list`` of ``abjad.Staff``.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

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
