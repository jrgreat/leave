import sys
import asyncio

async def hello():
    print("hello,world!")
    await asyncio.sleep(1)
    print("hello,again")

async def hello(name):
    print("hello,world!, from {}".format(name))
    await asyncio.sleep(1)
    print("hello,again, from {}".format(name))

def coroutine():
    print("start coroutine!")
    while True:
        try:
            x = yield
        except Exception as e :
            print("exception is [{}]".format(e))
            break
        else:
            print("x is [{}]".format(x))
        finally:
            print("coroutine ended!")

def call_corotine():
    my_co = coroutine()
    next(my_co)
    for i in range(11):
        my_co.send(i)
        if i == 10:
            my_co.throw(Exception)
    my_co.close()

async def main():
    L=await asyncio.gather(hello("bob"), hello("Alice"))
    print(L)

if __name__=="__main__":
    asyncio.run(main())
    
