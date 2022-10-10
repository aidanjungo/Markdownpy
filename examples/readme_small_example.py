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