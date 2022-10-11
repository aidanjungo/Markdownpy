from markdownpy.markdownpy import MarkdownDoc, Link
from pathlib import Path

md = MarkdownDoc("../README.md")

md.p(
    "[![PyPi version](https://img.shields.io/pypi/v/markdownpy.svg)](https://pypi.python.org/pypi/markdownpy)",
    no_new_line=True,
)
md.p(
    "[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/aidanjungo/Markdownpy/blob/main/LICENSE)",
    no_new_line=True,
)
md.p(
    "[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)",
    no_new_line=True,
)

md.h1("Markdownpy")

md.p("Simple Python package to write Markdown document directly from a Python script.")

md.image_custom("logo/markdownpy_logo.png", height=300, align="center")

md.h2("Install")

md.h3("Locally")
md.p("Clone the repository install it with pip:")
install_commands = """git clone git@github.com:aidanjungo/Markdownpy.git
cd Markdownpy
pip install -e ."""
md.code(install_commands, "bash")

md.h3("From PyPi")
md.p("You can install the last version of `Markdownpy` with pip:")
md.code("pip install markdownpy", "python")

md.h2("Usage")
md.p(
    "You can import and use the package in any Python script and use it to generate result or "
    "documentation files on the fly."
)

small_example = Path("readme_small_example.py").read_text()
md.code(small_example, "python")


example_link = Link("example.py", "examples/example.py")
md.p(f"From more example, checkout {example_link}")

readme_script_link = Link("readme.py", "examples/readme.py")
md.p(
    "By the way, this README has been generated using `Markdownpy`, "
    f"you can see the python script here: {readme_script_link}"
)

md.save()
