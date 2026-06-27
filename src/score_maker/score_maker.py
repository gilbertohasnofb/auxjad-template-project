from .compile_ly_file import compile_ly_file
from .create_staves import create_staves
from .final_tweaks import final_tweaks
from .generate_lilypond_file_structure import generate_lilypond_file_structure
from .generate_materials import generate_materials
from .generate_segments import generate_segments
from .prettify_score import prettify_score
from .print_header import print_header


def score_maker() -> None:
    r"""
    Generates the music and creates the final score.

    Args:
        None

    Returns:
        None
    """
    # Header
    print_header()

    # Creating music
    staves, instrument_properties = create_staves()
    materials_dict = generate_materials()
    generate_segments(materials_dict, staves)
    prettify_score(staves)

    # Generating LilyPond file structure
    lilypond_file, score = generate_lilypond_file_structure(instrument_properties)

    # Adding indicators and other text
    final_tweaks(instrument_properties, score)

    # Outputting score
    compile_ly_file(lilypond_file)
