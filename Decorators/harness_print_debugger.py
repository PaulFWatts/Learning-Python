from print_debugger import print_debugger


@print_debugger
def add(a, b):
    return a + b


seven = add(3, 4)
print(seven)
