
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

#hanoi
def move(n, a, b, c):
    if n==1:
        print("move [{}] --> [{}]".format(a,c))
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1,b, a, c)

if __name__=="__main__":
    move(3, 'x','y','z')