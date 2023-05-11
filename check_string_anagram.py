"""
Given two strings s1 and s2, write a Python function that returns True if s1 and s2 are anagrams of each other and False otherwise.

Example: race --> care
"""


def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


assert check_anagram('car', 'acr') == True
assert check_anagram('house', 'housa') == False
