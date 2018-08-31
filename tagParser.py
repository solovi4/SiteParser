import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    text = ""
    tags = []
    is_find = False

    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
            self.is_find = True

    def handle_endtag(self, tag):
        if tag in self.tags:
            self.text += "\n\n"
            self.is_find = False

    def handle_data(self, data):
        if self.is_find and len(data) > 0:
            self.text += data
            if not data.endswith(" "):
                self.text += " "


def get_text_from_tags(text_from_site, tags):
    parser = MyHTMLParser()
    parser.tags = tags
    parser.feed(text_from_site)
    return parser.text
