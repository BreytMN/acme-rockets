import os
from pathlib import Path

from .. import IS_SUBMODULE, SUBMODULE_PATH
from ._base_paths import STATIC_DIRECTORY_NAME, TEMPLATES_DIRECTORY_NAME
from .favicon import FAVICON_INPUT_PATH as FAVICON_INPUT_PATH
from .favicon import FAVICON_OUTPUT_FOLDER
from .tailwindcss import TAILWINDCSS_INPUT_PATH as TAILWINDCSS_INPUT_PATH
from .tailwindcss import TAILWINDCSS_OUTPUT_PATH

DEPLOY_MODE = int(os.environ.get("STATIC_BUILD", 0))
DYNAMIC_BUILD = not DEPLOY_MODE

TAILWINDCSS_INPUT_APP_PATH = Path("app", TAILWINDCSS_INPUT_PATH)
TAILWINDCSS_OUTPUT_APP_PATH = Path("app", TAILWINDCSS_OUTPUT_PATH)
FAVICON_INPUT_APP_PATH = Path("app", FAVICON_INPUT_PATH)

FAVICON_OUTPUT_APP_FOLDER = Path("app", FAVICON_OUTPUT_FOLDER)

STATIC_DIRECTORY_PATH = Path("app", STATIC_DIRECTORY_NAME)
TEMPLATES_DIRECTORY_PATH = Path("app", TEMPLATES_DIRECTORY_NAME)

if IS_SUBMODULE:
    STATIC_DIRECTORY_PATH = Path(SUBMODULE_PATH).joinpath(STATIC_DIRECTORY_PATH)
    TEMPLATES_DIRECTORY_PATH = Path(SUBMODULE_PATH).joinpath(TEMPLATES_DIRECTORY_PATH)
