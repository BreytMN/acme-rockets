import json
import os
import pathlib
from typing import Any, TypeAlias

DATA = pathlib.Path("data")
DEPENDENCIES = ["nav_links", "rockets", "testimonials"]

jsonl: TypeAlias = list[dict[str, Any]]


def dependencies() -> dict[str, list[dict[str, Any]]]:
    """
    Acme Rockets dependencies
    """

    return {dep: _read_jsonl(DATA.joinpath(f"{dep}.jsonl")) for dep in DEPENDENCIES}


def _read_jsonl(path: os.PathLike) -> jsonl:
    """
    Parse file in jsonl format to a list of dicts.
    """

    with open(path, "r") as f:
        return [json.loads(line) for line in f.readlines()]
