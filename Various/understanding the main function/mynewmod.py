# I only want to print when this module is run directly as a stand alone program and not imported

if __name__ == "__main__":
    print("This is my new module")

# _name_ is an attribute outside module, acts as a global inside the program
print(f'Hello from {__name__}!')

# x and y are global variables

x = 100

y = [10, 20, 30]
