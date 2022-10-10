from markdownpy.markdownpy import MarkdownDoc, Link
from pathlib import Path

md = MarkdownDoc("../README.md")

md.h1("Markdownpy")

md.p("Simple Python package to write Markdown document directly from a Python script.")

md.image_custom("logo/markdownpy_logo.png",height=300, align="center")

md.h2("Install")

md.h3("Locally")
md.p("Clone the repository install it with pip:")
install_commands = """git clone git@github.com:aidanjungo/Markdownpy.git
cd Markdownpy
pip install -e ."""
md.code(install_commands, "bash")

md.h3("From PyPi")
md.p("The package is not publish yet on Pypi.")

md.h2("Usage")
md.p("You can import and use the package in any Python script and use it to generate result or documentation filse on the fly.")

small_example = Path("readme_small_example.py").read_text()
md.code(small_example,"python")


example_link = Link("example.py","examples/example.py")
md.p(f"From more example, checkout {example_link}")

md.save()
