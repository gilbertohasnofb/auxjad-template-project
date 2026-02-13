import tomli

from .create_staves import create_staves
from .generate_materials import generate_materials
from .generate_segments import generate_segments
from .prettify_score import prettify_score
from .generate_lilypond_file_structure import generate_lilypond_file_structure
from .add_large_time_signatures import add_large_time_signatures
from .add_instrument_names import add_instrument_names
from .add_initial_clefs import add_initial_clefs
from .add_tempo_and_final_tweaks import add_tempo_and_final_tweaks
from .compile_ly_file import compile_ly_file


def score_maker():
    r"""
    Generates the music and creates the final score.

    Args:
        None

    Returns:
        None
    """
    # reading config.toml file
    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    # Header
    TITLE = config_dict["header"]["title"]
    print()
    print(TITLE)
    print("=" * len(TITLE))
    print()

    # Creating music
    staves, instrument_properties = create_staves()
    dict_of_materials = generate_materials()
    generate_segments(dict_of_materials, staves)
    prettify_score(staves)

    # Generating LilyPond file structure
    lilypond_file, score = generate_lilypond_file_structure(instrument_properties)

    # Adding indicators and other text
    add_instrument_names(instrument_properties)
    add_initial_clefs(instrument_properties)
    add_tempo_and_final_tweaks(staves, score)
    add_large_time_signatures(staves, score)

    # Outputting score
    compile_ly_file(lilypond_file)
