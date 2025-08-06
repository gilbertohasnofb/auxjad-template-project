import random
from typing import Optional, Tuple

import abjad
import auxjad
from tqdm import tqdm

from .. import tools
from .. import materials


def make_segment_B(*,
                   seed: Optional[int] = None,
                   ) -> Tuple[abjad.Staff]:
    r"""
    Makes segment B.

    Arguments:
        seed: optional integer for random seed

    Returns:
        tuple of abjad.Staff's
    """
    
    print('* Generating Segment B')
    
    if seed:
        random.seed(seed)

    segment_B_music = [
        abjad.Staff(r"\times 2/3 {ef'4 gf'4 af'4 ~} af'4 \times 2/3 {ef'4 gf'4 af'4 ~} af'4"),
        abjad.Staff(r"<df''' ef'''>2. <df''' ef'''>2."),
        abjad.Staff(r"r4 gf'2 r4 gf'2"),
        abjad.Staff(r"<df, ef,>2. <df, ef,>2."),
        abjad.Staff(r"gf'2 df'4 gf'2 df'4"),
        abjad.Staff(r"R1 * 3/4 R1 * 3/4"),
        abjad.Staff(r"ef2. ef2."),
    ]

    for staff in segment_B_music:
        abjad.attach(abjad.TimeSignature((3, 4)), abjad.select(staff).leaf(0))

    return segment_B_music
