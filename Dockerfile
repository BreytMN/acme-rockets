FROM python:3.12.3-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    APP_PATH="/opt/app" \
    APP="app" \
    STATIC_BUILD=1

WORKDIR $APP_PATH

COPY ${APP}/ requirements.txt ${APP_PATH}/

RUN pip install uv==0.1.37 && uv pip install --system -r requirements.txt; \
    tailwindcss_install && python -m build && uv pip uninstall --system pytailwindcss; \
    rm requirements.txt build.py tailwind.config.js && rm -rf .venv/lib/pytailwindcss/;

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
