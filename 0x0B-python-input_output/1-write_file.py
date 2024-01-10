#!/usr/bin/python3
"""defining write_file function """


def number_of_lines(filename=""):
    """write filename with utf-8"""
    with open(filename, encoding='utf-8') as f:
        return f.write(text)
