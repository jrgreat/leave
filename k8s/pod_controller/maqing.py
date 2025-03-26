from __future__ import division

import time

time1=time.time()

number=1000

number1=number + 10
b = 10**number1

x1 = b*4//5
x2=b//-239

he=x1+x2
number*=2

for i in range(3, number, 2):
    x1//=-25
    x2 //= -57121
    x=(x1+x2)//i
    he += x
pai = he*4

pai//=10**10
paistring=str(pai)
result=paistring[0] + str('.') + paistring[1:len(paistring)]
print(result)

time2=time.time()
print("total time: {}s".format(str(time2-time1)))