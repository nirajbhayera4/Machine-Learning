print("-----------------sync programming----------------")
import time
def task1():
    print("task 1 started")
    time.sleep(2)
    print("task 1 completed")

def task2():
    print("task 2 started")
    time.sleep(3)
    print("task 2 completed")
    
task1()
task2()

print("-----------------async programming----------------")
import asyncio
async def task1():
    print("task 1 start")
    await asyncio.sleep(2)
    print("task 1 completed")
async def task2():
    print("task 2 start")
    await asyncio.sleep(3)
    print("task 2 completed")
async def main():
    await asyncio.gather(task1(),task2())
    print("all tasks completed")
asyncio.run(main())

print("----API example----")
import aiohttp
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()
async def main():
    urls=[
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]
    async with aiohttp.ClientSession() as session:
        result=await asyncio.gather(*[fetch_data(session, url) for url in urls])
        for data in result:
            print(len(data))
asyncio.run(main())