# Markdownpy

Simple Python package to write Markdown document directly from a Python script.

<div align=center><img src="logo/markdownpy_logo.png" alt="" height=300/></div>

## Install

### Locally

Clone the repository install it with pip:

```bash
git clone git@github.com:aidanjungo/Markdownpy.git
cd Markdownpy
pip install -e .
```

### From PyPi

You can install the last version of `Markdownpy` with pip:

```python
pip install markdownpy
```

## Usage

You can import and use the package in any Python script and use it to generate result or documentation filse on the fly.

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

By the way, this README has been generate using `Markdownpy`, you can see the python script here: [readme.py](examples/readme.py)

