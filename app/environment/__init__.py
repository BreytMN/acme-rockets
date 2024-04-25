from pathlib import Path

from ._base_paths import STATIC_DIRECTORY_NAME as STATIC_DIRECTORY_NAME
from ._base_paths import TEMPLATES_DIRECTORY_NAME as TEMPLATES_DIRECTORY_NAME
from .favicon import FAVICON_INPUT_PATH as FAVICON_INPUT_PATH
from .favicon import FAVICON_OUTPUT_FOLDER
from .tailwindcss import TAILWINDCSS_INPUT_PATH as TAILWINDCSS_INPUT_PATH
from .tailwindcss import TAILWINDCSS_OUTPUT_PATH

LOGS_FOLDER_NAME = "logs"
JSONL_LOGS_PATH = Path(LOGS_FOLDER_NAME, "logs.jsonl")


def static_paths() -> dict[str, str]:
    """
    Returns a dict containing the paths to be used in the
    HTML links for the css and favicon files
    """

    return {
        "tailwindcss": str(TAILWINDCSS_OUTPUT_PATH),
        "favicon": str(FAVICON_OUTPUT_FOLDER),
    }
