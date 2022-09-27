#!/usr/bin/env python3
"""
Write a function that takes a string and returns a dictionary of the counts of each word in the string. Make sure the
function works well with mixed case words and ignores punctuation.
"""
import re
from collections import Counter


def count_words(sentence):
    """Count the number of times each word appears in a string."""
    words = re.findall(r"[\w']+", sentence.lower())
    return Counter(words)


print(count_words("oh what a day, what a lovely day!"))
print(count_words("don't stop believing"))
