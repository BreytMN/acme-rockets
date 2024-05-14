FROM python:3.12.3-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    APP_PATH="/opt/src" \
    APP="app" \
    STATIC_BUILD=1

WORKDIR $APP_PATH

COPY build.py requirements.txt tailwind.config.js ${APP_PATH}/
COPY ${APP} ${APP_PATH}/${APP}

RUN pip install uv==0.1.43 && uv pip install --system -r requirements.txt; \
    tailwindcss_install && python -m build && uv pip uninstall --system pytailwindcss; \
    rm build.py requirements.txt tailwind.config.js && rm -rf .venv/lib/pytailwindcss/;

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
