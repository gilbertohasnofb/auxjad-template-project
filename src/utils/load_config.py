import tomllib
from pathlib import Path
from typing import Any


def load_config(
    config_path: Path | str = Path(__file__).parent.parent / "config" / "config.toml",
) -> dict[str, Any]:
    r"""
    Load and return a TOML configuration file as a dictionary.

    Args:
        config_path (Path | str): Either a ``Path`` or a ``str`` object with path for the TOML
            config file. Defaults to Path(__file__).parent.parent / "config" / "config.toml".

    Returns:
        A ``dict`` containing the parsed configuration.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    if isinstance(config_path, str):
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("rb") as f:
        return tomllib.load(f)
