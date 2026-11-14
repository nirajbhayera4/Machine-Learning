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