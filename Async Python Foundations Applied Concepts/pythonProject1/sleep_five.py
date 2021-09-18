import asyncio


async def sleep_five():
    print('Starts sleep 5 secs')
    await asyncio.sleep(5)
    print('Finished sleep 5 secs')
    return 5


async def sleep_three_then_five():
    print('Starts sleep 3 seconds')
    await asyncio.sleep(3)
    print('Finished sleep 3 seconds')
    await sleep_five()
    return 8


async def main():
    res = await asyncio.gather(sleep_five(), sleep_three_then_five())
    print(res)


asyncio.run(main())
