from environment._base_paths import STATIC_ASSETS, STATIC_SRC

filename_input = "favicon.zip"
folder_ouput = "favicon"

FAVICON_INPUT_PATH = STATIC_SRC.joinpath(filename_input)
FAVICON_OUTPUT_FOLDER = STATIC_ASSETS.joinpath(folder_ouput)
