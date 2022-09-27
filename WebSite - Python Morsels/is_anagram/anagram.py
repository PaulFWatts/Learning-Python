#!/usr/bin/env python3
"""
Write a function that takes two strings and returns True if they are anagrams of each other and False otherwise.
Bonus 1: Make sure the function ignores spaces.
Bonus 2: Make sure the function ignores punctuation.


"""
import re
from collections import Counter
from itertools import zip_longest
from string import ascii_lowercase
from typing import Dict, List, Tuple


def is_anagram(word1: str, word2: str) -> bool:
    """Return True if word1 and word2 are anagrams of each other."""
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = re.sub(r"[^\w]", "", word1)
    word2 = re.sub(r"[^\w]", "", word2)
    return Counter(word1) == Counter(word2)


# Base problem
print(is_anagram("tea", "eat"))
print(is_anagram("tea", "treat"))
print(is_anagram("sinks", "skin"))
print(is_anagram("Listen", "silent"))
print()

# Bonus 1
print(is_anagram("coins kept", "in pockets"))
print()

# Bonus 2
print(is_anagram("a diet", "I'd eat"))
print()



