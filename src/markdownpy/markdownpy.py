"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
----------------------------------------------------------------------
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------
Author: Aidan Jungo
"""


class MarkdownDoc:
    def __init__(self, path):
        self.file = open(path, "w")

    def save(self):
        """Save the Markdown document"""
        if self.file:
            self.file.close()
            self.file = None

    def h1(self, text):
        """Add H1 title to the Markdown document"""

        self.file.write("# " + text)
        self.file.write("\n\n")

    def h2(self, text):
        """Add H2 title to the Markdown document"""

        self.file.write("## " + text)
        self.file.write("\n\n")

    def h3(self, text):
        """Add H3 title to the Markdown document"""

        self.file.write("### " + text)
        self.file.write("\n\n")

    def h4(self, text):
        """Add H4 title to the Markdown document"""

        self.file.write("#### " + text)
        self.file.write("\n\n")

    def h5(self, text):
        """Add H5 title to the Markdown document"""

        self.file.write("##### " + text)
        self.file.write("\n\n")

    def h6(self, text):
        """Add H6 title to the Markdown document"""

        self.file.write("###### " + text)
        self.file.write("\n\n")

    def p(self, text):
        """Add paragraph to the Markdown document"""

        self.file.write(text)
        self.file.write("\n\n")

    def blist(self, mylist: list):
        """Add bullet list to the Markdown document"""

        for item in mylist:
            self.file.write("- " + item)
            self.file.write("\n")
        self.file.write("\n")

    def nlist(self, mylist: list):
        """Add numbered list to the Markdown document"""

        for item in mylist:
            self.file.write("1. " + item)
            self.file.write("\n")
        self.file.write("\n")

    def code(self, code, language=""):
        """Add code block to the Markdown document"""

        self.file.write("```" + language + "\n")
        self.file.write(code)
        self.file.write("\n")
        self.file.write("```")
        self.file.write("\n\n")

    def line(self, n=1):
        """Add separation line(s) to the Markdown document"""
        for i in range(n):
            self.file.write("---")
            self.file.write("\n\n")

    def image(self, path, alt_text=""):
        """Add image to the Markdown document"""

        self.file.write("![" + alt_text + "](" + str(path) + ")")

    def image_custom(self, path, alt_text="", height=None, width=None, align=None):
        """Add image with custom settings to the Markdown document"""

        html_img = f'<img src="{path}" alt="{alt_text}"'

        if height:
            html_img += f" height={height}"
        if width:
            html_img += f" width={width}"

        html_img += "/>"

        if align:
            html_img = f"<div align={align}>" + html_img + "</div>"

        self.file.write(html_img)
        self.file.write("\n\n")


class Link:
    """Class to save a link and be able to place it in text."""

    def __init__(self, name, url):
        """
        Args:
            name (str): Link displayed name
            url (str): Link URL
        """
        self.name = name
        self.url = url

    def __str__(self):
        return "[" + self.name + "](" + self.url + ")"


class Reference:
    """Class to save a references and be able to cite them it in text and write it down."""

    _ids = set()

    def __init__(self, id, description):
        """
        Args:
            id (str): Reference id (e.g. AIAA22)
            description (str): Referenrce description(e.g. Author, Title, Journal, Date)
        """

        if id in Reference._ids:
            raise ValueError(f"{id} is already used!")
        self.id = id
        Reference._ids.add(id)

        self.idx = len(Reference._ids)

        self.description = description

    def cite(self):
        """Cite a reference in text"""

        return f"[[{self.idx}]]({self.id})"

    def write(self):
        """Write down a reference"""

        return f'<a id="{self.id}">[{self.idx}]</a> ' + self.description
