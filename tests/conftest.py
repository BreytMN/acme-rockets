import os
import shutil
from zipfile import ZipFile


def pytest_sessionstart(session):
    with open("app/static/style/output.css", "w") as f:
        f.write("something")

    with ZipFile("app/static/src/favicon.zip", "r") as zip:
        zip.extractall("app/static/assets/favicon")


def pytest_sessionfinish(session, exitstatus):
    os.remove("app/static/style/output.css")
    shutil.rmtree("app/static/assets/favicon")
