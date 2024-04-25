import os
import shutil
import sys
from zipfile import ZipFile

SYSPATH = "./app"
sys.path.insert(0, SYSPATH)


def pytest_sessionstart(session):
    os.chdir(SYSPATH)

    with open("static/style/output.css", "w") as f:
        f.write("something")

    with ZipFile("static/src/favicon.zip", "r") as zip:
        zip.extractall("static/assets/favicon")


def pytest_sessionfinish(session, exitstatus):
    os.chdir(SYSPATH)

    os.remove("static/style/output.css")
    shutil.rmtree("static/assets/favicon")
