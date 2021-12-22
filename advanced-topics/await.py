#Font: https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/

print("#Async/Await")
print()

import pdb

print("#Trying to run Async directly")

async def speak_async():
    for i in range(100):
        print("Hello I'm Anderson, writer on CFG")
        
speak_async()

print()

print("#Coroutine using Event Loop")

import asyncio

async def function_asyc():
    for i in range(5):
        print("Hello, I'm Anderson")
        print("GFG is Great")
    return 0
    
#loop1 = asyncio.get_event_loop()
#loop1.run_until_complete(function_asyc())
#loop1.close()
print("HELLO WORLD")
print("HELLO WORLD")

print()

print("#More thant one function at a time")

async def function_1():
    for i in range(100000):
        if i % 5000 == 0:
            print("Hello, I'm Anderson")
            print("GFG is Great")
    return 0

async def function_2():
    print("\n HELLO WORLD \n")
    return 0
    
async def main():
    f1 = loop.create_task(function_1())
    f2 = loop.create_task(function_2())
    await asyncio.wait([f1,f2])

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#loop.close()

print()

print("#Runing coroutines in background")

async def function_1():
    i = 0

    while True:
        i += 1
        if i % 5000 == 0:
            print("Hello, I'm Anderson")
            print("GFG is Great")
            await asyncio.sleep(0.01)

async def function_2():
    while True:
        await asyncio.sleep(0.01)
        print("\n HELLO WORLD \n")

#loop = asyncio.get_event_loop()
#asyncio.ensure_future(function_1())
#asyncio.ensure_future(function_2())
#loop.run_forever()

print()
