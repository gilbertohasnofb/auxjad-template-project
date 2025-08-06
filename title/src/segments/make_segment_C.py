import random
from typing import Optional, Tuple

import abjad
import auxjad
from tqdm import tqdm

from .. import tools
from .. import materials


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
    
    print('* Generating Segment C')
    
    if seed:
        random.seed(seed)

    segment_C_music = [
        abjad.Staff(r"a''4 g''2 f''4 e''2 a''4 g''2 f''4 e''2"),
        abjad.Staff(r"r2. <f'' a''>2. r2. <f'' a''>2."),
        abjad.Staff(r"<a' e' d'>1 r2 <a' e' d'>1 r2"),
        abjad.Staff(r"r2 <f a>1  ~ <f a>2 <f a>1 "),
        abjad.Staff(r"a''4 g''2 f''4 e''2 a''4 g''2 f''4 e''2"),
        abjad.Staff(r"d1. d1."),
        abjad.Staff(r"d,2 r1 d,2 r1"),
    ]

    for staff in segment_C_music:
        abjad.attach(abjad.TimeSignature((3, 2)), abjad.select(staff).leaf(0))

    return segment_C_music
