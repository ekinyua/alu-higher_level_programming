#!/usr/bin/python3
# function that appends a string at the end of a text file (UTF8),
# and returns the number of characters added
"""
    define a function 'append_write'
"""

def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)