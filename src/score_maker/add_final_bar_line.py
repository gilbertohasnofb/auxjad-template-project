import abjad


def add_final_bar_line(
    score: abjad.Score,
) -> None:
    r"""
    Adds final bar line to the staves.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    print("* Adding Final Bar Line:", end=" ")

    score.add_final_bar_line()

    print("Done")
