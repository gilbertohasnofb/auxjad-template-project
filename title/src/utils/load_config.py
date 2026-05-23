import tomllib
from pathlib import Path
from typing import Any


def load_config(path: str = "./src/config/config.toml") -> dict[str, Any]:
    r"""
    Load and return a TOML configuration file as a dictionary.

    Args:
        path: ``str` with path for the TOML config file. Defaults to "./src/config/config.toml".

    Returns:
        A ``dict`` containing the parsed configuration.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with config_path.open("rb") as f:
        return tomllib.load(f)
