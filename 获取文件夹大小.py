import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    a = getdirsize('G:\pyproject\gitfiles\HelloWorld')
    print(a / 1024 / 1024)
