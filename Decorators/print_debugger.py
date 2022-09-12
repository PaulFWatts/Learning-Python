def print_debugger(f):
    def new_function(*args, **kwargs):
        print(f"Calling {f.__name__} with {args = } and {kwargs = }.")
        ret = f(*args, **kwargs)
        print(f"Done with result = {ret}.")
        return ret
    return new_function
