import asyncio
from datetime import datetime
from pprint import pprint

import aiohttp
import click

urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
    "http://httpbin.org/get?text=you",
    "http://httpbin.org/get?text=can",
    "http://httpbin.org/get?text=almost",
    "http://httpbin.org/get?text=do",
    "http://httpbin.org/get?text=anything",
    "http://httpbin.org/get?text=with",
    "http://httpbin.org/get?text=it",
]  # 12 requests


async def get_args(session: aiohttp.ClientSession, url):
    async with session.get(url) as response:
        data = await response.json()
        return data['args']


async def main():
    list_of_request = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            list_of_request.append(get_args(session, url))
        results = await asyncio.gather(*list_of_request)
        pprint(results)


start = datetime.now()
asyncio.run(main())
click.secho(f'{datetime.now() - start}', bold=True, bg='blue', fg='white')
