import os
import shutil

import abjad
import tomli


def compile_ly_file(
        lilypond_file: abjad.LilyPondFile,
    ) -> None:
    r"""
    Creates list of staves and list of instrument properties (staves, instrument names, clefs,
        etc.).

    Arguments:
        lilypond_file: abjad.LilyPondFile created by generate_lilypond_file_structure()
        composition_filename: str with the filename of the composition
        root_directory: str with the composition root directory 

    Returns
        None
    """
    print('Compiling .ly file')
    print('------------------')
    print()

    # reading config.toml file
    with open('./src/config/config.toml', 'rb') as f:
        config_dict = tomli.load(f)

    # filename
    OUTPUT_FILENAME = config_dict['filename']['output_filename']

    # creating build directory
    if os.path.exists('./src/build'):
        print('Directory ./src/build already exists, removing it')
        shutil.rmtree('./src/build')
    print('Creating directory ./src/build')
    os.mkdir('./src/build')
    print()

    # copying .ily files to build directory
    try:
        os.mkdir('./src/build/includes')
    except:
        print('Directory ./src/build/includes already exists')
        print()
    finally:
        shutil.copyfile('./src/includes/stylesheet.ily',
                        './src/build/includes/stylesheet.ily',
                        )
    
    # generating files
    abjad.persist.as_pdf(
        lilypond_file,
        f'./src/build/{OUTPUT_FILENAME}.pdf',
    )

    # confirm build successful
    if os.path.exists(f'./src/build/{OUTPUT_FILENAME}.pdf'):
        print('Success')
    else:
        print('Something went wrong, build was not successful')
    print()
