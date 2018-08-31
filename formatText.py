def format_text(text, limit):
    i=0
    limit_counter = 0;
    last_space = 0;
    format_text = ""

    while i < len(text):
        char = text[i]
        if char == ' ':
            last_space = i

        if char == '\n':
            limit_counter = 0

        if limit_counter>=limit:
            format_text += text[:last_space] + "\n"
            text = text[last_space+1:]
            i = 0;
            limit_counter = 0;

        i += 1
        limit_counter += 1

    format_text += text
    return format_text
