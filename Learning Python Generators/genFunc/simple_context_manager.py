from contextlib import contextmanager


@contextmanager
def simple_cm(n):
    try:
        print(f'setup {n}')
        yield n + 1
    finally:
        print(f'wrap up {n}')


if __name__ == '__main__':
    with simple_cm(10) as n:
        print(f'do job {n}')
