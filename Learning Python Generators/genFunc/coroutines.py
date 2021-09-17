def coroutine_example():
    while True:
        x = yield
        # do some work with x
        print(x)


if __name__ == '__main__':
    cr = coroutine_example()
    cr.__next__()
    cr.send(4)
