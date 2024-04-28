import os

__version__ = "1.1.1"
title = "Acme Rockets"

APP_INFO = {
    "title": title,
    "version": __version__,
    "summary": "Landing Page using FastAPI in backend and Tailwindcss in the frontend",
}

IS_SUBMODULE = int(os.environ.get("SUBMODULES", 0))
SUBMODULE_PATH = "acme_rockets"
