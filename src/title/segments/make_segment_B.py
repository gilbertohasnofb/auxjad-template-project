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
    
    print('* making Segment B')
    
    if seed:
        random.seed(seed)

    segment_B_music = [
        abjad.Staff(r"\times 2/3 {ef'2 gf'2 af'2}"),
        abjad.Staff(r"<df''' ef'''>1"),
        abjad.Staff(r"r4 gf'2."),
        abjad.Staff(r"<df, ef,>1"),
        abjad.Staff(r"gf'2 df'2"),
        abjad.Staff(r"R1"),
        abjad.Staff(r"ef1"),
    ]

    return segment_B_music
