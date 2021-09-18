import asyncio
from datetime import datetime

import click


async def sleep_and_print(seconds):
    print(f'starting {seconds} sleep starts...')
    await asyncio.sleep(seconds)
    print(f'finishing sleep {seconds} ')
    return seconds


async def main():
    results = await asyncio.gather(
        sleep_and_print(3),
        sleep_and_print(4),
        sleep_and_print(5),
        sleep_and_print(6))
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="blue", fg="white")
