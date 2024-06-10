# Convert HTML to MARKDOWN 

DIV_CLASSES_TO_IGNORE = [
    'captioned-button-wrap', # share card
    'subscription-widget-wrap' # subscribe card
]

class ProcessHTML():
    def process_children(self, tag):
        if not tag.contents:
            return ""
        if isinstance(tag.contents, str):
            return tag.contents
        para = ""
        for i in tag.contents:
            if i.name:
                method = getattr(self, i.name)
                para += method(i)
            else: # string
                para += i
        return para 

    def p(self, tag):
        content = self.process_children(tag)
        return f"{content} \n\n"
    def strong(self, tag):
        content = self.process_children(tag)
        return f"**{content.strip()}**"
    def em(self, tag):
        content = self.process_children(tag)
        return f"_{content.strip()}_"
    def s(self, tag):
        content = self.process_children(tag)
        return f"~~{content.strip()}~~"
    def a(self, tag):
        content = self.process_children(tag)
        link = tag['href']
        return f"[{content}]({link})"
    def blockquote(self, tag):
        content = self.process_children(tag)
        result = ""
        for i in content.split("\n"):
            result += "> {i} \n"
        return content
    def hr(self, tag):
        return "\n--- \n"
    def br(self, tag):
        return "\n"
    def div(self, tag):
        for class_name in tag.get('class', []):
            if class_name in DIV_CLASSES_TO_IGNORE:
                return ""
        content = self.process_children(tag)
        return f'{content}'
    def h1(self, tag):
        content = self.process_children(tag)
        return f"# {content} \n"
    def h2(self, tag):
        content = self.process_children(tag)
        return f"## {content} \n"
    def h3(self, tag):
        content = self.process_children(tag)
        return f"### {content} \n"
    def h4(self, tag):
        content = self.process_children(tag)
        return f"#### {content} \n"
    def h5(self, tag):
        content = self.process_children(tag)
        return f"##### {content} \n"
    def h6(self, tag):
        content = self.process_children(tag)
        return f"###### {content} \n"
    def ul(self, tag):
        content = ""
        for child_tag in tag.contents:
            if child_tag.name == "li":
                content += f"- {self.li(child_tag)} \n"
        return content
    def ol(self, tag):
        content = ""
        index = 1
        for child_tag in tag.contents:
            if child_tag.name == "li":
                content += f"{index}. {self.li(child_tag)} \n"
                index += 1
        return content
     
    # ignore tags
    def form(self, tag):
        return ""
    def svg(self, tag):
        return ""
    def figure(self, tag):
        return ""
    
    # only process children
    def span(self, tag):
        content = self.process_children(tag)
        return content
    def li(self, tag):
        content = self.process_children(tag)
        return content 


def process_substack_html(html_soup):
    markdown_content = ""
    title = html_soup.find("h1", class_="post-title")
    markdown_content += f'# {title.string} \n'

    sub_title = html_soup.find("h3", class_="subtitle")
    markdown_content += f'{sub_title.string} \n\n'

    content = html_soup.find("div", class_="available-content")
    article_content = content.div
    # content_list = content.div.contents
    markdown_content += f'{ProcessHTML().p(article_content)}\n\n'
    with open('output.md', mode='w') as f:
        f.write(markdown_content)
