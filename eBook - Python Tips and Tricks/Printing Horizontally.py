"""
When looping over an iterable, the print function prints each
item in the new line. This is because the print function has a
parameter called end. By default, the end parameter has an
escape character (end =’\n’). To print horizontally, we need to
remove the escape character and replace it with an empty string
(end = “ “)
"""
# Print horizontally
for i in range(1, 11):
    print(i, end=" ")

# Print vertically
print()
for i in range(1, 11):
    print(i)

# Print vertically with a separator
for i in range(1, 11):
    print(i, end=" | ")
