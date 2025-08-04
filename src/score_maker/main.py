import tomli

from .create_staves import create_staves
from .generate_and_add_segments_to_staves import generate_and_add_segments_to_staves
from .prettify_score import prettify_score
from .generate_lilypond_file_structure import generate_lilypond_file_structure
from .add_large_time_signatures import add_large_time_signatures
from .add_instrument_names import add_instrument_names
from .add_initial_clefs import add_initial_clefs
from .add_tempo_and_final_tweaks import add_tempo_and_final_tweaks
from .stylesheet_generator import stylesheet_generator
from .compile_ly_file import compile_ly_file


def main():
    r"""
    Generates the music and creates the final score.

    Arguments:
        None

    Returns:
        None
    """
    # reading config.toml file
    with open('./config/config.toml', 'rb') as f:
        config_dict = tomli.load(f)

    # Header
    TITLE = config_dict['header']['title']
    print()
    print(TITLE)
    print('=' * len(TITLE))
    print()

    staves, instrument_properties = create_staves()
    generate_and_add_segments_to_staves(staves)
    prettify_score(staves)
    lilypond_file, score = generate_lilypond_file_structure(instrument_properties)
    # add_large_time_signatures(staves, score)
    add_instrument_names(instrument_properties)
    add_initial_clefs(instrument_properties)
    add_tempo_and_final_tweaks(staves, score)
    stylesheet_generator()
    compile_ly_file(lilypond_file)
