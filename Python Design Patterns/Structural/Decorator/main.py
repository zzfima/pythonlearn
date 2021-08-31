from decorator import hello_world

if __name__ == '__main__':
    # Check the result of decorating
    res = hello_world()
    print(res)

    # Check if the function name is still the same name of the function being decorated
    print(hello_world.__name__)

    # Check if the docstring is still the same as that of the function being decorated
    print(hello_world.__doc__)
