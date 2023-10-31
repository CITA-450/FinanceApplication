
# FlaskCdrx

 --first web page

# to RUN as ADMIN from PowerShell

install :
pip install sqlalchemy
pip install flask
pip install flask-login
pip install flask-sqlalchemy
<<<<<<< HEAD
 pip install git+https://github.com/maxcountryman/flask-login.git  
=======
pip install Werkzeug
>>>>>>> 25d15a0f9c80848a608e8bdf8db8a08a606758b7

# try this if you are having issus:pip install git+https://github.com/maxcountryman/flask-login.git  

# Python 3 (python)

Develop Python 3 applications.

## Options

| Options Id | Description | Type | Default Value |
|-----|-----|-----|-----|
| imageVariant | Python version (use -bookworm, or -bullseye variants on local arm64/Apple Silicon): | string | 3.11-bullseye |

This template references an image that was [pre-built](https://containers.dev/implementors/reference/#prebuilding) to automatically include needed devcontainer.json metadata.

* **Image**: mcr.microsoft.com/devcontainers/python ([source](https://github.com/devcontainers/images/tree/main/src/python))
* **Applies devcontainer.json contents from image**: Yes ([source](https://github.com/devcontainers/images/blob/main/src/python/.devcontainer/devcontainer.json))

## Installing or updating Python utilities

This container installs all Python development utilities using [pipx](https://pipxproject.github.io/pipx/) to avoid impacting the global Python environment. You can use this same utility add additional utilities in an isolated environment. For example:

```bash
pipx install prospector
```

See the [pipx documentation](https://pipxproject.github.io/pipx/docs/) for additional information.

---

_Note: This file was auto-generated from the [devcontainer-template.json](https://github.com/devcontainers/templates/blob/main/src/python/devcontainer-template.json).  Add additional notes to a `NOTES.md`._
