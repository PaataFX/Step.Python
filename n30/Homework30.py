import asyncio

async def print_numbers():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)

async def hello_world():
    await asyncio.sleep(2)
    print("Hello World!!!")

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(hello_world())
    
    # Wait for both tasks to complete
    await task1
    await task2

asyncio.run(main())
