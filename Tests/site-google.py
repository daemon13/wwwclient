#!/usr/bin/env python
# vim: tw=80 ts=4 sw=4 noet
from os.path import join, basename, dirname, abspath
import _import
from wwwclient import browse, scrape
HTML = scrape.HTML

s = browse.Session("http://www.google.com")
f = s.form().fill(q="python web scraping")
s.submit(f, action="btnG", method="GET")

tree  = scrape.HTML.tree(s.page())
nodes = tree.cut(below=3)
nodes = nodes.filter(accept=lambda n:n.name.lower() in ("table","p"))
for node in nodes.children:
	print HTML.text(node)
	if node.name == "p":
		link = node.find(withName="a")[0]
		print "-->", link.attribute("href")
		print HTML.links(link)
	else:
		print "---------"

# Google results are not properly closed, so we had to identify patterns where
# there were  a closing tag should be inserted
# close_on = ("td", "a", "img", "br", "a")
# scrape.do(scrape.HTML.iterate, session.last().data(), closeOn=close_on, write=sys.stdout)
# EOF
