import abjad
import tomli
from tqdm import tqdm

from .. import segments


def generate_and_add_segments_to_staves(staves: list[abjad.Staff]) -> None:
    r"""
    Generates musical materials from segments and adds them to the staves.

    Args:
        staves: ``list`` of ``abjad.Staff``'s.

    Returns:
        None
    """
    print("Generating musical segments")
    print("---------------------------")
    print()

    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    SEGMENT_PARAMS = config_dict["segments"]

    list_of_segments = []
    for segment_name, segment_maker in zip(SEGMENT_PARAMS.keys(), segments.list_of_segments):
        print(f"- Generating: {segment_name}")
        segment = segment_maker(**SEGMENT_PARAMS[segment_name])
        list_of_segments.append(segment)
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
