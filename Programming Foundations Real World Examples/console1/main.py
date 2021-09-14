name = 'koko'


def print_hi(*attrs):
    print(len(attrs))
    print(name)


def print_bye():
    global name
    name = 'lolo'
    print(name)


if __name__ == '__main__':
    print_hi('dsd', 'dsd', 'fff')
    print_bye()
    print_hi()
