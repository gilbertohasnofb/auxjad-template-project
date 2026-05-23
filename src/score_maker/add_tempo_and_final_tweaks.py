import abjad


def add_tempo_and_final_tweaks(
    staves: list[abjad.Staff],
    score: abjad.Score,
) -> None:
    r"""
    Adds tempo marking, final bar line, and other final tweaks to the staves.

    Args:
        staves: ``list`` of ``abjad.Staff``'s.
        score: ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    # tempo markup (defined as a LilyPond variable in stylesheet)
    tempo_markup = abjad.LilyPondLiteral(r"\tempo-markup")
    for staff in staves:
        abjad.attach(tempo_markup, abjad.select(staff).leaf(0))

    # adding pedal marks and initial dynamics
    # <... code ...>

    # adding final bar
    score.add_final_bar_line()
