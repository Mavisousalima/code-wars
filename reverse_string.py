"""
Given a String, return its reverse

Example:
reverse_string("Hello") --> "olleh"
"""


def reverse_string(word):
    return word[::-1]


assert reverse_string('Hello') == 'olleH'
