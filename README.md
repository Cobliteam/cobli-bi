# Cobli - BI

## Installing

### Dependencies

Current production version of python interpreter is 3.9.6, so it is recommended to use same python version in your
development environment.

### On the terminal

It's recommended to use [python vitual environments](https://docs.python.org/pt-br/3/library/venv.html) to deal with
dependencies per-project.

After clonning the project, just execute inside project root:

```sh
python -m venv venv
```

To activate it:

```sh
source venv/bin/activate
```

All project related commands are intended to be execute inside this virtual environment

To get out of a virtual environment:

```sh
deactivate
```

Installing dependencies and running application locally:

First, create a .env file and write

```sh
API_KEY={your-api-key}
```

Then, run this command on terminal

```sh
pip install -r src/requirements.txt -r src/requirements-dev.txt
python src/my_script.py
```
