from pathlib import Path

import abjad

from ..utils import load_config
from .stylesheet_generator import stylesheet_generator


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
    config_dict = load_config()

    # filename and directories
    OUTPUT_FILENAME = config_dict["filename"]["output_filename"].replace(" ", "_")
    BUILD_DIR = Path("build")
    INCLUDES_DIR = BUILD_DIR / "includes"
    OUTPUT_PATH = BUILD_DIR / f"{OUTPUT_FILENAME}.pdf"

    # creating build directory
    print(f"* Creating directory ./{BUILD_DIR}")
    BUILD_DIR.mkdir(exist_ok=True)

    # copying .ily files to build directory
    print(f"* Creating directory ./{INCLUDES_DIR}")
    INCLUDES_DIR.mkdir(exist_ok=True)
    print()

    # generate style sheet
    stylesheet_generator()

    # generating files
    abjad.persist.as_pdf(lilypond_file, OUTPUT_PATH)

    # confirm build successful
    if OUTPUT_PATH.exists():
        print(f"Success! Score created as ./{OUTPUT_PATH}")
    else:
        print("Something went wrong, build was not successful...")
    print()
