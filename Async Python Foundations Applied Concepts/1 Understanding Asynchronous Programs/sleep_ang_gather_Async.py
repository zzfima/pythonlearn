import asyncio
from datetime import datetime

import click


async def sleep_and_print(seconds):
    print(f'starting {seconds} sleep starts...')
    await asyncio.sleep(seconds)
    print(f'finishing sleep {seconds} ')
    return seconds


async def main():
    coroutines_list = []
    for i in range(3, 7):
        coroutines_list.append(sleep_and_print(i))
    results = await asyncio.gather(*coroutines_list)

    # results = await asyncio.gather(
    #     sleep_and_print(3),
    #     sleep_and_print(4),
    #     sleep_and_print(5),
    #     sleep_and_print(6))
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="blue", fg="white")
