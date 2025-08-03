import random
from typing import Optional, Tuple

import abjad
import auxjad
from tqdm import tqdm

from .. import tools
from .. import materials


def make_segment_A(*,
                   seed: Optional[int] = None,
                   ) -> Tuple[abjad.Staff]:
    r"""
    Makes segment A.

    Arguments:
        seed: optional integer for random seed

    Returns:
        tuple of abjad.Staff's
    """
    
    print('* making Segment A')
    
    if seed:
        random.seed(seed)

    segment_A_music = [
        abjad.Staff(r"c''4 d''4 e''4 f''4"),
        abjad.Staff(r"c'4 d'4 e'4 f'4"),
        abjad.Staff(r"c2 g2"),
        abjad.Staff(r"c''4 d''4 e''4 f''4"),
        abjad.Staff(r"c,2 g,2"),
        abjad.Staff(r"c,1"),
    ]

    return segment_A_music
