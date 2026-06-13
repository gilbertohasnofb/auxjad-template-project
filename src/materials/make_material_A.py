import random

import abjad

from .material_A_definitions import RANDOM_SEED


def make_material_A() -> list[abjad.Staff]:
    r"""
    Generates Material A for Segment #1.

    Args:
        None

    Returns:
        list[abjad.Staff]: List of staves, each with their respective materials.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

    material = [
        abjad.Staff([abjad.Note(random.randint(12, 24), (1, 4)) for _ in range(4)]),
        abjad.Staff([abjad.Note(random.randint(12, 24), (1, 4)) for _ in range(4)]),
        abjad.Staff([abjad.Note(random.randint(0, 12), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(0, 12), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
        abjad.Staff([abjad.Note(random.randint(-12, 0), (1, 2)) for _ in range(2)]),
    ]

    return material
