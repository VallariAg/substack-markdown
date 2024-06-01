# Convert HTML to MARKDOWN 

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
    def h4(self, tag):
        pass


def process_substack_html(html_soup):
    title = html_soup.find("h1", class_="post-title")
    print(title.string)

    sub_title = html_soup.find("h3", class_="subtitle")
    print(sub_title.string)

    content = html_soup.find("div", class_="available-content")
    content_list = content.div.contents

    for tag in content_list:
        if tag.name == "p":
            print(ProcessHTML().p(tag))
