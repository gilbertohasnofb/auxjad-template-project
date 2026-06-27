import abjad


def add_initial_tempo(
    score: abjad.Score,
) -> None:
    r"""
    Adds tempo markings to the staves.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    print("* Adding Initial Tempo:", end=" ")

    # tempo markup (defined as a LilyPond variable in stylesheet)
    tempo_markup = abjad.LilyPondLiteral(r"\tempo-markup")
    for staff in abjad.iterate(score).components(abjad.Staff):
        abjad.attach(tempo_markup, abjad.select(staff).leaf(0))

    print("Done")
