from sys import argv
from functools import partialmethod
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# url = 'https://vallariagrawal.substack.com/p/curious-minds-1-why-do-pricing-usually'
url = argv[1]

req = Request(
    url=url,
    headers={'User-Agent': 'Mozilla/5.0'}
)
html = urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

class ProcessHTML():
    def p(self, tag):
        para = ""
        for i in tag.contents:
            if i.name:
                method = getattr(self, i.name)
                para += method(i)
            else: # string
                para += i
        return para

    def span(self, tag):
        return tag.string
    def strong(self, tag):
        return f"**{tag.string}**"
    def em(self, tag):
        return f"_{tag.string}_"
    def s(self, tag):
        return f"~{tag.string}~"
    def a(self, tag):
        return ""



title = soup.find("h1", class_="post-title")
print(title.string)

sub_title = soup.find("h3", class_="subtitle")
print(sub_title.string)


content = soup.find("div", class_="available-content")
content_list = content.div.contents

for tag in content_list:
    if tag.name == "p":
        print(ProcessHTML().p(tag))


