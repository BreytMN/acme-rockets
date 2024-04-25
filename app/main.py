from typing import Annotated, Any

from __init__ import app_info
from dependencies import dependencies
from environment import STATIC_DIRECTORY_NAME, TEMPLATES_DIRECTORY_NAME, static_paths
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from helpers import lifespan

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}


app = FastAPI(**app_info, lifespan=lifespan)
app.add_middleware(CORSMiddleware, **CORS_CONFIG)
app.mount(f"/{STATIC_DIRECTORY_NAME}", StaticFiles(directory=STATIC_DIRECTORY_NAME))
templates = Jinja2Templates(TEMPLATES_DIRECTORY_NAME)


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
        "static": static_paths,
        **app_info,
        **dependencies,
    }

    params = {
        "request": request,
        "name": "index.html",
        "context": context,
    }

    return templates.TemplateResponse(**params)
