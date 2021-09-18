import asyncio
import time


async def my_func():
    await fff()


async def fff():
    await kkk()


async def kkk():
    ggg()


def ggg():
    time.sleep(5)
    print("work")


if __name__ == '__main__':
    print("hello")
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(my_func())
    loop.run_forever()
    loop.close()
    print("bye")
