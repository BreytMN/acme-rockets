import os
import shutil
import subprocess  # nosec
from contextlib import asynccontextmanager
from zipfile import ZipFile

from environment import (
    FAVICON_INPUT_PATH,
    FAVICON_OUTPUT_FOLDER,
    TAILWINDCSS_INPUT_PATH,
    TAILWINDCSS_OUTPUT_PATH,
)
from fastapi import FastAPI

DEPLOY_MODE = int(os.environ.get("STATIC_BUILD", 0))
DYNAMIC_BUILD = not DEPLOY_MODE


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Re-run the build and cleanup if not in deploy mode
    """

    if DYNAMIC_BUILD:
        build()

    yield

    if DYNAMIC_BUILD:
        cleanup()


def build():
    _install_zip(FAVICON_INPUT_PATH, FAVICON_OUTPUT_FOLDER)
    _build_tailwind(TAILWINDCSS_INPUT_PATH, TAILWINDCSS_OUTPUT_PATH)


def cleanup():
    shutil.rmtree(FAVICON_OUTPUT_FOLDER)
    os.remove(TAILWINDCSS_OUTPUT_PATH)


def _install_zip(input: os.PathLike, output: os.PathLike):
    with ZipFile(input, "r") as zip:
        zip.extractall(output)


def _build_tailwind(input: os.PathLike, output: os.PathLike):
    command = ["tailwindcss", "-i", str(input), "-o", str(output), "--minify"]
    subprocess.run(command)  # nosec
