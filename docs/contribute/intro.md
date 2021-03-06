# Contribute to this project

✨ Welcome we're excited you're here and want to contribute. ✨

:::{admonition} Be sure to check out our Code of Conduct
This project and its community follows [this Code of Conduct](../CODE_OF_CONDUCT.md) to ensure that our online spaces are enjoyable, inclusive, and productive for all contributors.
:::

## Getting started (contributing to this site)

### Setting your local environment

To get started with the codebase, take the following steps:

1. Clone the repository, from your terminal:

    ```bash
    git clone https://github.com/Quansight-Labs/jupyter-a11y-mgmt
    ```

2. Install needed dependencies

    We recommend using Python `3.8` to build the project as it is the version we are currently using to deploy the site.

    ```bash
    # Install nox
    pip install nox --user
    ```

3. Build and serve the site locally with `nox`

    ```bash
    nox --session live_docs
    ```

    Running this command will install `jupyter-book` in a virtual environment and build the output in `docs/_build`.
    Runnign this command will use [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) to build the documentation site and start watching for changes in `docs/`.
    It will also start a server at  `http://localhost:8000/`.

🎉  Once you have your server up and running you can head to [http://127.0.0.1:5500/](http://127.0.0.1:5500/) on your web browser of choice and get started.

To stop the server you will need to type <kbd> Ctrl + C </kbd> on your terminal.
