import asyncio

async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )

asyncio.run(main())