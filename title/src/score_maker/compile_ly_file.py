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

    Args:
        lilypond_file: ``abjad.LilyPondFile`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    print("Compiling .ly file")
    print("------------------")
    print()

    # reading config.toml file
    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    # filename
    OUTPUT_FILENAME = config_dict["filename"]["output_filename"]

    # creating build directory
    print("- Creating directory ./build")
    try:
        os.mkdir("./build")
    except:
        print("- Directory ./build already exists")
    print()

    # copying .ily files to build directory
    print("- Creating directory ./build/includes")
    try:
        os.mkdir("./build/includes")
    except:
        print("- Directory ./build/includes already exists")
        print()
    finally:
        shutil.copyfile(
            "./src/includes/stylesheet.ily",
            "./build/includes/stylesheet.ily",
        )

    # generating files
    abjad.persist.as_pdf(
        lilypond_file,
        f"./build/{OUTPUT_FILENAME}.pdf",
    )

    # confirm build successful
    if os.path.exists(f"./build/{OUTPUT_FILENAME}.pdf"):
        print("Success")
    else:
        print("Something went wrong, build was not successful")
    print()
