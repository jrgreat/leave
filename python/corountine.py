import sys

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


if __name__=="__main__":
    my_co = coroutine()
    next(my_co)
    for i in range(11):
        my_co.send(i)
        if i == 10:
            my_co.throw(Exception)
    my_co.close()
