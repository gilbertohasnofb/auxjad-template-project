from .auxiliary_score_maker_functions import *


def main():
    r"""
    Generates the music and creates the final score.

    Arguments:
        None

    Returns:
        None
    """
    COMPOSITION_FILENAME = 'title'  # RENAME title
    COMPOSITION_ROOT_DIRECTORY = './title'  # RENAME title
    
    staves, instrument_properties = create_staves(composition_filename=COMPOSITION_FILENAME)
    generate_and_add_segments_to_staves(staves)
    prettify_score(staves)
    lilypond_file, score = generate_lilypond_file_structure(instrument_properties)
    # add_large_time_signatures(staves, score)
    add_instrument_names(instrument_properties)
    add_initial_clefs(instrument_properties)
    add_tempo_and_final_tweaks(staves, score)
    compile_ly_file(lilypond_file,
                    composition_filename=COMPOSITION_FILENAME,
                    composition_root_directory=COMPOSITION_ROOT_DIRECTORY,
                    )


