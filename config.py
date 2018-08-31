import os


class MyConfig:
    chars_in_line = None
    tags = None

    def __init__(self, chars_in_line, tags):
        self.chars_in_line = chars_in_line
        self.tags = tags


def load_config():
    path_to_file = os.getcwd()+"/config.ini"
    default_tags =  {"p", "h1", "h2", "h3"}
    default_chars_in_line = 80
    if os.path.isfile(path_to_file):
        f = open("config.ini", 'r')
        lines = f.readlines()
        f.close()
        chars_in_line = None
        tags = None
        for line in lines:
            if line.startswith("charsInLine"):
                chars_in_line = line[line.index("=")+1:]
                chars_in_line = chars_in_line.strip()
                try:
                    chars_in_line = int(chars_in_line)
                except ValueError:
                    chars_in_line = default_chars_in_line
                continue

            if line.startswith("tags"):
                tags = line[line.index("=")+1:]
                tags = tags.split(",")
                tags_strip = [];
                for tag in tags:
                    tags_strip.append(tag.strip())
                tags = tags_strip
                continue

        if chars_in_line is None:
            chars_in_line = default_chars_in_line
        if tags is None:
            tags = default_tags

        return MyConfig(chars_in_line, tags)
    else:
        return MyConfig(default_chars_in_line, default_tags)
