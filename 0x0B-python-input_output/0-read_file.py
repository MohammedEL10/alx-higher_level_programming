#!/usr/bin/python3
"""reads a text file (UTF8)"""


def read_file(filename=""):
    with open("filename", encoding="UTF8")as f:
        print(f.read(), end="")
