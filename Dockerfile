FROM python:3.13.3-alpine3.21 AS builder

ENV PYTHONOPTIMIZE=2 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_PATH="/opt/src" \
    APP="app" \
    TAILWINDCSS_VERSION="v3.4.17" \
    STATIC_BUILD=1

WORKDIR $APP_PATH

COPY build.py requirements.txt tailwind.config.js ${APP_PATH}/
COPY ${APP} ${APP_PATH}/${APP}

RUN pip install uv==0.1.43 && \
    uv pip install --system -r requirements.txt && \
    python -m build

FROM python:3.13.3-alpine3.21

ENV PYTHONUNBUFFERED=1 \
    APP_PATH="/opt/src" \
    APP="app" \
    STATIC_BUILD=1

WORKDIR $APP_PATH

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY --from=builder ${APP_PATH}/${APP} ${APP_PATH}/${APP}

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]