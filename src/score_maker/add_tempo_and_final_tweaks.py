import abjad


def add_tempo_and_final_tweaks(
    score: abjad.Score,
) -> None:
    r"""
    Adds tempo marking, final bar line, and other final tweaks to the staves.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    # tempo markup (defined as a LilyPond variable in stylesheet)
    tempo_markup = abjad.LilyPondLiteral(r"\tempo-markup")
    for staff in score:
        abjad.attach(tempo_markup, abjad.select(staff).leaf(0))

    # adding pedal marks and initial dynamics
    # <... code ...>

    # adding final bar
    score.add_final_bar_line()
