import os
from unittest.mock import patch

import pytest

from app.helpers import build, cleanup


@pytest.fixture
def temp_paths(tmp_path):
    test_favicon_folder = tmp_path / "test_favicon"
    test_tailwind_folder = tmp_path / "test_tailwind_output"
    test_favicon_folder.mkdir()
    test_tailwind_folder.mkdir()

    return {
        "favicon_folder": test_favicon_folder,
        "tailwind_file": test_tailwind_folder.joinpath("style.css"),
    }


def test_build(temp_paths):
    with patch("app.helpers.FAVICON_OUTPUT_FOLDER", temp_paths["favicon_folder"]):
        with patch("app.helpers.TAILWINDCSS_OUTPUT_PATH", temp_paths["tailwind_file"]):
            build()

    for f in temp_paths.values():
        assert os.path.exists(f)


def test_cleanup(temp_paths):
    with open(temp_paths["tailwind_file"], "w") as f:
        f.write("something")

    with patch("app.helpers.FAVICON_OUTPUT_FOLDER", temp_paths["favicon_folder"]):
        with patch("app.helpers.TAILWINDCSS_OUTPUT_PATH", temp_paths["tailwind_file"]):
            cleanup()

    for f in temp_paths.values():
        assert not os.path.exists(f)
