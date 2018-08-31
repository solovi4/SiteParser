from urllib.request import urlopen
from tagParser import get_text_from_tags
from formatText import format_text


def get_text(url, conf):
    page = urlopen(url)
    charset = page.headers.get_content_charset()
    alltext = page.read().decode(charset);
    clear_text = get_text_from_tags(alltext, conf.tags)
    formated_text = format_text(clear_text, conf.chars_in_line)
    return formated_text;
