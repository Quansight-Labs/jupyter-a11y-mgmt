from nox import session

# Nox sessions are defined here, if you are running these locally you might want
# to run each session individually, for example
# nox --sessions docs


@session(reuse_venv=True)
def docs(session):
    """Docs session - it installs the needed dependencies
    and build the JupyterBook"""
    session.install("jupyter-book")
    session.run("jupyter-book", "build", "docs")


@session(reuse_venv=True)
def serve(session):
    """Docs session - it installs the needed dependencies
    and build the JupyterBook"""
    session.run(
        "python", "-m", "http.server", "8000", "--directory", "docs/_build/html/"
    )
