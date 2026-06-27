from .. import utils
from .compile_ly_file import compile_ly_file
from .create_staves import create_staves
from .final_tweaks import final_tweaks
from .generate_lilypond_file_structure import generate_lilypond_file_structure
from .generate_materials import generate_materials
from .generate_segments import generate_segments
from .prettify_score import prettify_score


def score_maker() -> None:
    r"""
    Generates the music and creates the final score.

    Args:
        None

    Returns:
        None
    """
    # Header
    utils.print_header()

    # Creating music
    staves, instrument_properties = create_staves()
    materials_dict = generate_materials()
    generate_segments(materials_dict, staves)
    prettify_score(staves)

    # Generating LilyPond file structure
    lilypond_file, score = generate_lilypond_file_structure(instrument_properties)

    # Adding indicators and other text
    final_tweaks(
        instrument_properties,
        score,
        add_instrument_names=True,
        add_initial_clefs=True,
        add_initial_tempo=True,
        add_large_time_signatures=True,
        add_final_bar_line=True,
        add_miscellaneous_tweaks=True,
    )

    # Outputting score
    compile_ly_file(lilypond_file)
