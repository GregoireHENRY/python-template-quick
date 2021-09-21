#!/usr/bin/env python3

"""
Goniometer.
"""

from pathlib import Path  # noqa: F401
from typing import Optional  # noqa: F401

import ruamel.yaml  # noqa: F401
from dotmap import DotMap  # noqa: F401
from pudb import set_trace as bp  # noqa: F401

CONFIG_FILE = Path("config.yaml")


def read_config(FILE_PATH: Path) -> DotMap:
    """Load the config file."""
    CFG, IND, BSI = ruamel.yaml.util.load_yaml_guess_indent(FILE_PATH.open())
    return DotMap(CFG)


def main() -> None:
    CFG = read_config(CONFIG_FILE)  # noqa: F841


if __name__ == "__main__":
    main()
