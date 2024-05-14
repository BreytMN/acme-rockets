# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2024-04-28

### Fixed

- App is now configured to be instaled into a `modules` folder if used as submodule.

### Added

- Alias `make server` for `make server-venv`.

### Changed

- Upgrade Dependencies: fastapi 0.111.0, uv==0.1.43, etc.

## [1.1.1] - 2024-04-28

### Fixed

- Submodule path now conforms to a valid python module.

## [1.1.0] - 2024-04-28

### Added

- Support to be used as submodule/subtree out-of-the-box.
- Rocket Favicon

### Changed

- Upgrade Dependencies: fastapi 0.110.2, pytest 8.2.0, etc.
- App now is started from root folder instead of app folder.

## [1.0.0] - 2024-04-25

### Added

- Acme Rockets landing page written with HTML, CSS and Tailwindcss.
- Backend written in FastAPI.
