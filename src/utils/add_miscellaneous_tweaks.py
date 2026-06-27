import abjad


def add_miscellaneous_tweaks(
    score: abjad.Score,
) -> None:
    r"""
    Adds miscellaneous tweaks to the staves.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    print("* Miscellaneous tweaks:", end=" ")

    # adding pedal marks to lower piano staff
    lower_piano_staff = score["Piano"]["Piano_Lower"]
    abjad.piano_pedal(
        abjad.select(lower_piano_staff).leaves(),
        half_pedal=True,
        until_the_end=True,
        omit_raise_pedal_glyph=True,
    )

    print("Done")
