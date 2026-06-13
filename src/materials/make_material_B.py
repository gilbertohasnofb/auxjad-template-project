import random

import abjad

from .material_B_definitions import RANDOM_SEED


def make_material_B() -> list[abjad.Staff]:
    r"""
    Generates Material B for Segment #2.

    Args:
        None

    Returns:
        list[abjad.Staff]: List of staves, each with their respective materials.
    """
    if RANDOM_SEED:
        random.seed(RANDOM_SEED)

    material = [
        abjad.Staff([abjad.Note(random.randint(12, 36), (1, 16)) for _ in range(12)]),
        abjad.Staff([abjad.Note(random.randint(12, 36), (1, 16)) for _ in range(12)]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Note(random.randint(-24, 0), (1, 8)) for _ in range(6)]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Rest((3, 4))]),
        abjad.Staff([abjad.Rest((3, 4))]),
    ]

    return material
