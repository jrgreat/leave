
#add 1 to 100
def add(x):
    if x == 0:
        return 0;
    else:
        return x + add(x-1)

#5! = ?
def jiecheng(x):
    if x==1:
        return 1;
    else:
        return x*jiecheng(x-1)

if __name__=="__main__":
    print(jiecheng(5))