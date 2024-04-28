import os
import shutil
import subprocess  # nosec
from contextlib import asynccontextmanager
from zipfile import ZipFile

from fastapi import FastAPI

from ..environment import (
    FAVICON_INPUT_APP_PATH,
    FAVICON_OUTPUT_APP_FOLDER,
    TAILWINDCSS_INPUT_APP_PATH,
    TAILWINDCSS_OUTPUT_APP_PATH,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Re-run the build and cleanup if not in deploy mode
    """

    build()

    yield

    cleanup()


def build():
    _install_zip(FAVICON_INPUT_APP_PATH, FAVICON_OUTPUT_APP_FOLDER)
    _build_tailwind(TAILWINDCSS_INPUT_APP_PATH, TAILWINDCSS_OUTPUT_APP_PATH)


def cleanup():
    shutil.rmtree(FAVICON_OUTPUT_APP_FOLDER)
    os.remove(TAILWINDCSS_OUTPUT_APP_PATH)


def _install_zip(input: os.PathLike, output: os.PathLike):
    with ZipFile(input, "r") as zip:
        zip.extractall(output)


def _build_tailwind(input: os.PathLike, output: os.PathLike):
    command = ("tailwindcss", "-i", str(input), "-o", str(output), "--minify")
    subprocess.run(command)  # nosec
