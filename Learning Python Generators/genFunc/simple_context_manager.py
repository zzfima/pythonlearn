from contextlib import contextmanager


@contextmanager
def simple_cm(n):
    try:
        print(f'setup {n}')
        yield
    finally:
        print(f'wrap up {n}')


if __name__ == '__main__':
    with simple_cm(10) as n:
        print('do job')
