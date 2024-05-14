# Acme Rockets

## Landing Page using FastAPI in backend and tailwindcss in the frontend

![Rocket Dab](app/static/img/rocketdab.png)

This project was heavily based on this [tutorial](https://github.com/gitdagray/tailwind-css-course) by [Dave Gray](https://www.youtube.com/watch?v=pYaamz6AyvU&list=PL0Zuz27SZ-6M8znNpim8dRiICRrP5HPft) with some important differences on the code:
 * Using [FastAPI](https://fastapi.tiangolo.com/) with [Jinja](https://palletsprojects.com/p/jinja/) templates as backend - this helps reducing repetition in the html and opens the doors for more backend features;
 * No javascript files - the script is written directly in the [html file](app/templates/layout/header.html);
 * As the [standalone installer](https://tailwindcss.com/blog/standalone-cli) provided by [pytailwindcss](https://pypi.org/project/pytailwindcss/) integrates with better with Python, that means no NPM is needed for [tailwindcss](https://tailwindcss.com/).

The resulting page works both on desktop and mobile browsers.

## Summary
* [Using this repo](#using-this-repo)
* [To do](#to-do)
* [License](#licence)

### About me

#### Links
* [E-mail](mailto:lunde@adobe.com)
* [GitHub](https://github.com/BreytMN)
* [LinkedIn](https://www.linkedin.com/in/breytner-nascimento/)
* [Portfolio](https://portfolio.breytmn.com)


## Using this repo

All the code can be run by make commands written in th [Makefile](Makefile)

### Prerequisites

This repository is written using WSL with an Ubuntu distro running Python `3.12`.

For [deployment](requirements.txt):
```txt
fastapi==0.111.0
jinja2==3.1.4
pytailwindcss==0.2.0
uvicorn==0.29.0
```

For [development](requirements_dev.txt):
```
mypy==1.10.0
pre-commit==3.7.1
ruff==0.4.4
watchfiles==0.21.0
```

For [testing](requirements_test.txt):
```txt
httpx==0.27.0
pytest==8.2.0
pytest-asyncio==0.23.6
pytest-cov==5.0.0
```

### Installing
Clone the repository:
```bash
git clone git@github.com:BreytMN/acme-rockets.git
```

I suggest using VS Code as text editor and IDE for navigating this repository. Open the folder inside VS Code after changing directory with:
```bash
cd acme-rockets
code .
```

### Running the server locally
If you do not have Python 3.12 installed, you can run this on terminal (tested on WSL - Ubuntu):
```bash
make python
```
This will install Python 3.12 and all dependencies need to run it, in the end it will prompt the user to set the default version for Python.

After that you can run:
```bash
make venv
source .venv/bin/activate
```
The first command will create a virtual environment and install all libraries needed to run any code inside this repository. The second command will activate the environment.

To run the unit tests:
```bash
make test
```
The output of the test with code coverage report will be displayed in the terminal.

To start the server:
```bash
make server
```
You can see the page on the browser through the link http://127.0.0.1:8000/

### Running the server through docker
Alternatively, you can skip all steps to run the server locally and use docker to build and run the app:
```bash
make server-docker
```

## To do
 * Make the "Contact Us" section actually send a post request to the server;
 * Look up for better ways to extract the components and partials from the html to avoid repetition even where it makes sense.


## Licence
[MIT License](LICENSE)