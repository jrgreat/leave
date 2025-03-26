
#add 1 to 100
def add(x):
    if x == 0:
        return 0;
    else:
        return x + add(x-1)

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

#hanoi
def move(n, a, b, c):
    if n==1:
        print("move [{}] --> [{}]".format(a,c))
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1,b, a, c)

def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fab(n-1) + fab(n-2)

def max_value(nums, i):
    if i == 1:
        return nums[i]
    return max(max_value(nums, i-1), nums[i])

def hanoi(n, A, B , C):
    """
    n: n disks
    A: pole A
    B: pole B
    C: pole C
    means move n disks from pole A to pole C through pole B
    """
    def move(n, A,C):
        """
        move disk from A to C
        """
        print("move disk {} from pole A to C".format(n))
    if n == 1:
        move(n, A, C)
    else:
        move(n-1,A, )
    


if __name__=="__main__":
    nums = [1,2,3,6,4,5]
    print(max_value(nums, 4))
    