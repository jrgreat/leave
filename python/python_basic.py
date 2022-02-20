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


if __name__=="__main__":
    snooze(3)