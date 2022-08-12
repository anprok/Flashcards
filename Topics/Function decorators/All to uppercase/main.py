def to_upper(other_func):
    def wrapper(args_for_function):
        return other_func(args_for_function.upper())

    return wrapper

