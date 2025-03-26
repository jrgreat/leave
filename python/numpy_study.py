import numpy as np

#print(np.__version__)
#np.show_config()
my_dict = dict()
for i in range(10):
    my_dict[str(i)] = i

def fun(x, *args, **kwargs):
    print(x)
    print(args)
    for key,value in kwargs.items():
        print(key, value)

list = [1,2,3,4]
fun(3, *list, my_dict)