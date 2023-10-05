import asyncio


async def test():
    print("BEFORE")
    await asyncio.sleep(5)
    print("AFTER")
    for i in range(1000):
        print(i)


asyncio.run(test())

