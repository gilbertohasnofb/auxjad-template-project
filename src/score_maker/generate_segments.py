import abjad
from tqdm import tqdm

from .. import segments


def generate_segments(
    materials_dict: dict[str, abjad.Container],
    staves: list[abjad.Staff],
) -> None:
    r"""
    Generates musical materials from segments and adds them to the staves.

    Args:
        materials_dict (dict[str, abjad.Container]): A ``dict`` containing names of materials as
            ``str`` and the materials themselves as ``abjad.Container``.
        staves (list[abjad.Staff]): A ``list`` of ``abjad.Staff``'s in which material will be added.

    Returns:
        None
    """
    print("Generating musical segments")
    print("---------------------------")
    print()

    list_of_segments = []
    with tqdm(total=len(segments.list_of_segment_makers)) as pbar:
        for segment_maker in segments.list_of_segment_makers:
            segment = segment_maker(materials_dict)
            list_of_segments.append(segment)
            pbar.update(1)
    print()

    print("Adding segments to staves")
    print("-------------------------")
    print()

    with tqdm(total=len(list_of_segments) * len(staves)) as pbar:
        for segment in list_of_segments:
            for staff, music in zip(staves, segment):
                staff.extend(music)
                pbar.update(1)
    print()
