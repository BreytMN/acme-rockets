import json
import os
import pathlib
from typing import Any, TypeAlias, Union

from . import IS_SUBMODULE, SUBMODULE_NAME, SUBMODULE_PATH
from .environment import (
    FAVICON_OUTPUT_FOLDER,
    STATIC_DIRECTORY_NAME,
    TAILWINDCSS_OUTPUT_PATH,
)

DATA = pathlib.Path("app", "data")
if IS_SUBMODULE:
    DATA = pathlib.Path(SUBMODULE_PATH).joinpath(DATA)

JSON_FILES = ("images",)
JSONLINES_FILES = ("nav_links", "rockets", "testimonials")

JSON_PATHS = {dep: DATA.joinpath(f"{dep}.json") for dep in JSON_FILES}
JSONLINES_PATHS = {dep: DATA.joinpath(f"{dep}.jsonl") for dep in JSONLINES_FILES}

jsonl: TypeAlias = list[dict[str, Any]]


def static_paths() -> dict[str, str]:
    """
    Returns a dict containing the paths to be used in the
    HTML head to insert the links for the css and favicon files
    """

    return {
        "tailwindcss": str(TAILWINDCSS_OUTPUT_PATH),
        "favicon": str(FAVICON_OUTPUT_FOLDER),
    }


def dependencies() -> dict[str, Union[dict[str, str], list[dict[str, Any]]]]:
    """
    Acme Rockets body dependencies
    """

    return {
        **{dep: _read_json(f) for dep, f in JSON_PATHS.items()},
        **{dep: _read_jsonlines(f) for dep, f in JSONLINES_PATHS.items()},
    }


def _read_json(path: os.PathLike) -> dict[str, str]:
    """
    Parse json files into dict
    """

    with open(path, "r") as f:
        data = json.loads(f.read())

    if IS_SUBMODULE:
        data = {key: _fix_static_path(value) for key, value in data.items()}
    return data


def _read_jsonlines(path: os.PathLike) -> jsonl:
    """
    Parse file in jsonl format to a list of dicts.
    """

    with open(path, "r") as f:
        lines = f.readlines()

    if IS_SUBMODULE:
        return [json.loads(_fix_static_path(line)) for line in lines]
    return [json.loads(line) for line in lines]


def _fix_static_path(
    line: str,
    static_folder: str = STATIC_DIRECTORY_NAME,
    submodule_name: str = SUBMODULE_NAME,
) -> str:
    """
    Add submodule prefix to the path
    """

    return line.replace(
        f"/{static_folder}/",
        f"/{submodule_name}/{static_folder}/",
    )
