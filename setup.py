#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

NAME = "markdownpy"
VERSION = "0.1.4"
AUTHOR = "Aidan Jungo"
EMAIL = "aidan.jungo@cfse.ch"
DESCRIPTION = "PyPI package to write Markdown document directly from a Python script"
LONG_DESCRIPTION = open("README.md").read()
URL = "https://github.com/aidanjungo/Markdownpy"
REQUIRES_PYTHON = ">=3.8.0"
REQUIRED = []
README = "README.md"
PACKAGE_DIR = "src"
LICENSE = "Apache License 2.0"

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    include_package_data=True,
    package_dir={"": PACKAGE_DIR},
    license=LICENSE,
    packages=[NAME],
    python_requires=REQUIRES_PYTHON,
    keywords=["Markdown", "Python", "documentation"],
    install_requires=REQUIRED,
    # See: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
)
