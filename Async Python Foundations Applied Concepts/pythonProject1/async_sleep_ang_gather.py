import time
from datetime import datetime

import click


def sleep_and_print(seconds):
    print(f'starting {seconds} sleep starts...')
    time.sleep(seconds)
    print(f'finishing sleep {seconds} ')
    return seconds


if __name__ == '__main__':
    start = datetime.now()
    print([sleep_and_print(3), sleep_and_print(6)])
    click.secho(f'{datetime.now() - start}', bold=True, bg='blue', fg='white')
