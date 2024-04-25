from environment._base_paths import STATIC_CSS, STATIC_SRC

filename_input = "input.css"
filename_output = "output.css"

TAILWINDCSS_INPUT_PATH = STATIC_SRC.joinpath(filename_input)
TAILWINDCSS_OUTPUT_PATH = STATIC_CSS.joinpath(filename_output)
