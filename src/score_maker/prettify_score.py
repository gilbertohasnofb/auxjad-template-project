import abjad
import auxjad
from tqdm import tqdm


def prettify_score(staves: list[abjad.Staff]) -> None:
    r"""
    Prettifies score (e.g. remove repeated time signatures, repeated dynamics, etc.)

    Args:
        staves (list[abjad.Staff]): A ``list`` of ``abjad.Staff``'s to be modified.

    Returns:
        None
    """
    print("Prettifying score")
    print("-----------------")
    print()

    with tqdm(total=len(staves)) as pbar:
        for staff in staves:
            leaves = abjad.select(staff).leaves()
            auxjad.mutate.remove_repeated_time_signatures(leaves)
            auxjad.mutate.remove_repeated_dynamics(leaves)
            auxjad.mutate.reposition_clefs(leaves)
            pbar.update(1)
    print()

    print("* Done")
    print()
