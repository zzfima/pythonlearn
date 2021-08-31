from functools import wraps


def make_blink(func):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(func)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        res = func()

        # Add new functionality to the function being decorated
        return "<blink>{}</blink>".format(res)

    return decorator


# Apply the decorator here!

@make_blink
def hello_world():
    """Original function! """

    return "Hello, World!"
