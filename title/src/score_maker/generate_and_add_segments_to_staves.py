from typing import List

import abjad
from tqdm import tqdm

from .. import segments


def generate_and_add_segments_to_staves(staves: List[abjad.Staff]) -> None:
    r"""
    Generates musical materials from segments and adds them to the staves.

    Arguments:
        staves: list of abjad.Staff's

    Returns
        None
    """
    print('Generating musical segments')
    print('---------------------------')
    print()

    list_of_segments = []
    for segment in segments.segment_factory():
        list_of_segments.append(segment)
    print()

    print('Adding segments to staves')
    print('-------------------------')
    print()

    with tqdm(total=len(list_of_segments) * len(staves)) as pbar:
        for segment in list_of_segments:
            for staff, music in zip(staves, segment):
                staff.extend(music)
                pbar.update(1)
    print()
