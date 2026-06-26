import abjad


def add_misc_tweaks(
    score: abjad.Score,
) -> None:
    r"""
    Adds miscelaneous tweaks to the staves.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    # adding pedal marks to lower piano staff
    lowest_piano_staff = score["Piano"]["Piano_Lower"]
    abjad.piano_pedal(
        lowest_piano_staff[:],
        half_pedal=True,
        until_the_end=True,
        omit_raise_pedal_glyph=True,
    )
