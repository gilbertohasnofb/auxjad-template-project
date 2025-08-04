from typing import List

import abjad
import auxjad
from tqdm import tqdm


def prettify_score(staves: List[abjad.Staff]) -> None:
    r"""
    Prettifies score (e.g. remove repeated time signatures, repeated dynamics, etc.)

    Arguments:
        staves: list of abjad.Staff's

    Returns
        None
    """
    # prettifying score
    print('Prettifying score')
    print('-----------------')
    print()

    with tqdm(total=len(staves)) as pbar:
        for staff in staves:
            auxjad.mutate.remove_repeated_time_signatures(staff[:])
            auxjad.mutate.remove_repeated_dynamics(staff[:])
            pbar.update(1)
    print()

    # manual fixes
    # print('Manual fixes')
    # print('------------')
    # print()
    #
    # <... code ...>
    # print()
