from nox import session


@session(reuse_venv=True)
def docs(session):
    session.install("jupyter-book")
    session.run("jb", "build", "docs", "--path-output=.",
                "--builder=singlehtml")
