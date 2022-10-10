# Markdownpy

<img align="right" width="300" height="300" src="logo/markdownpy_logo.png">

Simple Python package to write Markdown document directly from a Python script.

## Install

### Locally

Clone the repository install it with pip:

```bash
git clone git@github.com:aidanjungo/Markdownpy.git
cd Markdownpy
pip install -e .
```

### From Pypi

The package is not publish yet on Pypi.

### Usage

You can import and use the package in any Python script and use it to generate result or documentation filse on the fly.

The following Python script:

```python
from markdownpy.markdownpy import MarkdownDoc

md = MarkdownDoc("MySimpleMarkdown.md")

md.h1("H1 title")
md.h2("H2 title")
md.p("paragraph")

md.h2("Lists")

mylist=[]
for i in range(5):
   mylist.append(f"item_{i}") 

md.blist(mylist)

md.save()
```

From more example, checkout [example.py](examples/example.py)
