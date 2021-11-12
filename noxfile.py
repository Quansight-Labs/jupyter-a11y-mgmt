from nox import session
from livereload import Server, shell

# Nox sessions are defined here, if you are running these locally you might want
# to run each session individually, for example
# nox --sessions docs


@session(reuse_venv=True)
def docs(session):
    """Docs session - it installs the needed dependencies
    and build the JupyterBook, recommended for CI"""
    session.install("jupyter-book", "livereload")
    session.run("jupyter-book", "build", "docs")


@session(reuse_venv=True)
def live_docs(session):
    """Live docs - build and serve the site, it will check for changes and reload the site"""
    session.install("jupyter-book", "livereload")
    session.run("jupyter-book", "build", "docs")
    server = Server()
    server.watch("docs/**", shell("jupyter-book build docs"))
    server.serve(root="docs/_build/html")
