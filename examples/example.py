from markdownpy.markdownpy import MarkdownDoc, Link, Reference
from pathlib import Path

mypath = Path("MyExample.md")

md = MarkdownDoc(mypath)

md.h1("H1 title")
md.h2("H2 title")
md.h3("H3 title")
md.h4("H4 title")
md.h5("H5 title")
md.h6("H6 title")
md.p("This is a paragraphe")
md.p("And another paragraphe")


md.h3("Lists")

md.p("Here's a bullet list:")
md.blist(["item1", "item2", "item3"])

md.p("Here's a numbered list:")
md.nlist(["item1", "item2", "item3"])


md.h3("Text and code block")

mycode = """import numpy as np
np.empty(20)"""
md.code(mycode, "python")

mytext = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Nobis, voluptatum molestias! A debitis natus tenetur incidunt 
fuga accusamus voluptatem nesciunt quis inventore adipisci, 
suscipit perspiciatis ducimus quae placeat rem nisi?"""
md.code(mytext)


md.h3("Formating")

md.p("You can use the same formating that you would use in a normal Markdown file.")
md.p("**bold**")
md.p("_italic_")
md.p("`monospace`")
md.p("~~strike~~")
md.p("<sub>sub</sub>")
md.p("<sup>sup</sup>")


md.h3("Links")

gh_link = Link("Github", "https://github.com")
md.p(f"This is the link to {gh_link}")

formating_link = Link("Formatting section", "#formating")
md.p(f"Link to the {formating_link}")


md.h3("Images")

md.image("../logo/markdownpy_logo.png", alt_text="Logo")

md.p("With `image_custom` you can define height, width, alignement")
md.image_custom(
    "../logo/markdownpy_logo.png", alt_text="Logo", height=125, width=422, align="center"
)


md.h3("Separation line")

md.line()

md.p("Multiple line in the same time")
md.line(3)


md.h3("Reference")

myref = Reference(
    "#JoR22",
    "Doe J., Title of a good reference, Journal of References, Volume 42, Number 3,  <https://google.com>",
)
myref2 = Reference(
    "#JoR23",
    "Doe J., Title of a good reference, Journal of References, Volume 43, Number 3,  <https://google.com>",
)
myref3 = Reference(
    "#JoR24",
    "Doe J., Title of a good reference, Journal of References, Volume 44, Number 6,  <https://google.com>",
)

md.p(f"This is my refs {myref.cite()}, {myref2.cite()},  {myref3.cite()} cite in a paragraph!")

md.p(myref.write())
md.p(myref2.write())
md.p(myref3.write())

md.save()
