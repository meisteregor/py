import sys
from os import walk, path


def your_wrapper(*args):
    for root, dirs, files in args[0]:
        for name in files:
            text = path.join(root, name)
            yield text
    return


lazy = your_wrapper(os.walk("c:\\"))
print(list(lazy))