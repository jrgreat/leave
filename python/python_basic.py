import time
import functools
registry = list()

def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

def make_averager():
    series = list()
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)


#@functools.cache
@clock
def fabonacci(n):
    if n<2:
        return n
    return fabonacci(n-2)*fabonacci(n-1)

def fun(alist):
    a = list()
    a[:] = alist
    a.append(3)
    print(alist)

def external():
    my_list = list()
    def use_list(value):
        my_list.append(value)
        x = 0
        for data in my_list:
            x = x + data
        return x
    return use_list

def d6():
    from random import randint
    return randint(1,6)

if __name__=="__main__":
    gen = (x for x in range(5))
    while True:
        print(next(gen))

    
    

