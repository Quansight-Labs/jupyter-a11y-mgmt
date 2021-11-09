from nox import session

# Nox sessions are defined here, if you are running these locally you might want
# to run each session individually, for example
# nox --sessions docs


@session(reuse_venv=True)
def docs(session):
    """Docs session for CI purposes - it installs the needed dependencies
    and build the JupyterBook"""
    session.install("jupyter-book")
    session.run("jb", "build", "docs", "--path-output=.", "--builder=singlehtml")
