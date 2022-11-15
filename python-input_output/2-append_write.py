#!/usr/bin/python3
"""
    define a function 'append_write'
"""

def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
