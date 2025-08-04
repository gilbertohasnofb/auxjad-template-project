import os
import shutil

import abjad


def compile_ly_file(
        lilypond_file: abjad.LilyPondFile,
        *,
        composition_filename: str,
        composition_root_directory: str,
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
    # creating build directory

    if os.path.exists(f'{composition_root_directory}/build'):
        print(f'Directory {composition_root_directory}/build already exists, removing it')
        shutil.rmtree(f'{composition_root_directory}/build')
    print(f'Creating directory {composition_root_directory}/build')
    os.mkdir(f'{composition_root_directory}/build')
    print()

    # copying .ily files to build directory
    try:
        os.mkdir(f'{composition_root_directory}/build/includes')
    except:
        print(f'Directory {composition_root_directory}/build/includes already exists')
        print()
    finally:
        shutil.copyfile(f'{composition_root_directory}/includes/stylesheet.ily',
                        f'{composition_root_directory}/build/includes/stylesheet.ily',
                        )
    
    # generating files
    abjad.persist.as_pdf(
        lilypond_file,
        f'{composition_root_directory}/build/{composition_filename}.pdf',
    )

    # confirm build successful
    if os.path.exists(f'{composition_root_directory}/build/{composition_filename}.pdf'):
        print('Success')
    else:
        print('Something went wrong, build was not successful')
    print()
