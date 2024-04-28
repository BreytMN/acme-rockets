from typing import Annotated, Any

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import APP_INFO, SUBMODULE_PATH
from .dependencies import dependencies, static_paths
from .environment import (
    DYNAMIC_BUILD,
    STATIC_DIRECTORY_NAME,
    STATIC_DIRECTORY_PATH,
    TEMPLATES_DIRECTORY_PATH,
)
from .helpers import lifespan

APP_CONFIG = {
    **APP_INFO,
    "lifespan": lifespan if DYNAMIC_BUILD else None,
}
CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}


app = FastAPI(**APP_CONFIG)
app.add_middleware(CORSMiddleware, **CORS_CONFIG)
app.mount(f"/{STATIC_DIRECTORY_NAME}", StaticFiles(directory=STATIC_DIRECTORY_PATH))
templates = Jinja2Templates(TEMPLATES_DIRECTORY_PATH)


@app.get("/", response_class=HTMLResponse)
def landing_page(
    request: Request,
    static_paths: Annotated[dict[str, str], Depends(static_paths)],
    dependencies: Annotated[dict[str, list[dict[str, Any]]], Depends(dependencies)],
):
    """
    Acme Rockets landing page
    """

    context = {
        **APP_INFO,
        **dependencies,
        "static": static_paths,
    }

    params = {
        "name": "index.html",
        "request": request,
        "context": context,
    }

    return templates.TemplateResponse(**params)


SUBMODULE_INFO = {"path": f"/{SUBMODULE_PATH}", "app": app}
