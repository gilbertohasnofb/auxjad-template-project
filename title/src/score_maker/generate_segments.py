import abjad
from tqdm import tqdm

from .. import segments


def generate_segments(
    dict_of_materials: dict[str, abjad.Container],
    staves: list[abjad.Staff],
) -> None:
    r"""
    Generates musical materials from segments and adds them to the staves.

    Args:
        dict_of_materials: ``dict`` containing names of materials as ``str`` and the materials
            themselves as ``abjad.Container``.
        staves: ``list`` of ``abjad.Staff``'s.

    Returns:
        None
    """
    print("Generating musical segments")
    print("---------------------------")
    print()

    list_of_segments = []
    with tqdm(total=len(segments.list_of_segment_makers)) as pbar:
        for segment_maker in segments.list_of_segment_makers:
            segment = segment_maker(dict_of_materials)
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
