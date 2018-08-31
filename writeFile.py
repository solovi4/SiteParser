import os


def write(file_name, text):
    if not os.path.exists(os.path.dirname(file_name)):
        dir_name = os.path.dirname(file_name)
        os.makedirs(dir_name)

    f = open(file_name, 'w')
    f.write(text)
    f.close()
    return None
