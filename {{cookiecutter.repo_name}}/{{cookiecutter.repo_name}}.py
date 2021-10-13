#!/usr/bin/env python3

"""
{{cookiecutter.project_name}}.
"""

from pathlib import Path
from typing import Optional  # noqa: F401

import ruamel.yaml
from dotmap import DotMap
from pudb import set_trace as bp  # noqa: F401

VERSION = "0.1.0"
CONFIG_FILE = Path("config.yaml")


def read_yaml(FILE_PATH: Path) -> DotMap:
    """Load the config file."""
    CFG, IND, BSI = ruamel.yaml.util.load_yaml_guess_indent(FILE_PATH.open())
    return DotMap(CFG)


def main() -> None:
    CFG = read_yaml(CONFIG_FILE)  # noqa: F841


if __name__ == "__main__":
    main()
