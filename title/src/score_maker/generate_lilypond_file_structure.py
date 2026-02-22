from collections import namedtuple

import abjad
import tomli


def generate_lilypond_file_structure(
    instrument_properties: list[namedtuple],
) -> tuple[abjad.LilyPondFile, abjad.Score]:
    r"""
    Creates the structure of the LilyPond file.

    Args:
        instrument_properties: ``list`` of ``namedtuples``, each with properties for an instrument.
            Must contain keys and values for ``container``for all staves and staff groups, generated
            by ``create_staves()``.

    Returns:
        ``Tuple`` containing an ``abjad.LilyPondFile`` and an ``abjad.Score`` objects.
    """
    print("Generating LilyPond file structure")
    print("----------------------------------")
    print()

    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    TEMPO_REFERENCE_NOTE = config_dict["tempo"]["tempo_reference_note"]
    TEMPO_VALUE = config_dict["tempo"]["tempo_value"]

    # creating score and appending instruments
    score = abjad.Score()
    for instrument in instrument_properties:
        score.append(instrument.container)

    # creating blocks and including stylesheet
    score_block = abjad.Block(name="score")
    layout_block = abjad.Block(name="layout")
    midi_block = abjad.Block(name="midi")
    midi_block.items.append(f"\\tempo {TEMPO_REFERENCE_NOTE} = {TEMPO_VALUE}")
    score_block.items.append(score)
    score_block.items.append(layout_block)
    score_block.items.append(midi_block)
    lilypond_file = abjad.LilyPondFile(
        items=[score_block],
        includes=["./includes/stylesheet.ily"],
    )

    print("- LilyPondFile successfully generated")
    print()

    return lilypond_file, score
