import random
from typing import Optional, Tuple

import abjad
import auxjad
from tqdm import tqdm

import tools
import materials


def make_segment_C(*,
                   seed: Optional[int] = None,
                   ) -> Tuple[abjad.Staff]:
    r"""
    Makes segment C.

    Arguments:
        seed: optional integer for random seed

    Returns:
        tuple of abjad.Staff's
    """
    
    print('* making Segment C')
    
    if seed:
        random.seed(seed)

    segment_C_music = [
        abjad.Staff(r"a''4 g''4 f''4 e''4 a''4 g''4 f''4 e''4"),
        abjad.Staff(r"r2 <f'' a''>2 r2 <f'' a''>2"),
        abjad.Staff(r"<a' e' d'>1 <a' e' d'>1"),
        abjad.Staff(r"r2 <f a>2  r2 <f a>2 "),
        abjad.Staff(r"a''4 g''4 f''4 e''4 a''4 g''4 f''4 e''4"),
        abjad.Staff(r"d1 d1"),
        abjad.Staff(r"d,2 r2 d,2 r2"),
    ]

    return segment_C_music
