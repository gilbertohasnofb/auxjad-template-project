from ..utils import load_config


def print_header() -> None:
    r"""
    Prints the header of the composition in the terminal during generation and score compilation.

    Args:
        None

    Returns:
        None
    """
    # reading config.toml file
    config_dict = load_config()

    # Header
    TITLE = config_dict["header"]["title"]
    COMPOSER = config_dict["header"].get("composer")
    YEAR = config_dict["header"].get("year")

    title = TITLE
    if YEAR is not None:
        title += f" ({YEAR})"

    print()
    print(title)
    print(COMPOSER)
    print("=" * 40)
    print()
