from fastapi.testclient import TestClient

from app.environment.favicon import FAVICON_OUTPUT_FOLDER
from app.environment.tailwindcss import TAILWINDCSS_OUTPUT_PATH
from app.main import app

client = TestClient(app)


def test_landing_page():
    response = client.get("/")

    assert response.status_code == 200
    assert str(TAILWINDCSS_OUTPUT_PATH) in response.text
    assert str(FAVICON_OUTPUT_FOLDER) in response.text
