import os


def get_path(url):
    url = url.strip()
    indexDoubleSlash = url.index("//");
    if indexDoubleSlash > -1:
        urlshort = url[indexDoubleSlash + 2:]

    if urlshort.endswith("/"):
        urlshort = urlshort[:len(urlshort)-1]
        return os.getcwd() + "/" + urlshort + ".txt"

    index_dot = urlshort.rindex(".")
    index_slash = urlshort.rfind("/")

    if index_dot < index_slash:
        return os.getcwd() + "/" + urlshort + ".txt"
    else:
        urlshort = urlshort[:index_dot]
        return os.getcwd() + "/" + urlshort + ".txt"
