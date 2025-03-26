def bubble_sort(to_be_sort_list):
    if not isinstance(to_be_sort_list, list):
        raise Exception("not a list!")
    n = len(to_be_sort_list)
    for i in range(n):
        for j in range(n-i-1):
            if to_be_sort_list[j] > to_be_sort_list[j+1]:
                to_be_sort_list[j], to_be_sort_list[j+1] = to_be_sort_list[j+1], to_be_sort_list[j]

    print(to_be_sort_list)


def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data)//2]
        left = list()
        right = list()
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


def insert_sort(data):
    n = len(data)
    for i in range(1,n):
        temp = data[i]
        j = i -1
        while j>=0 and temp < data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = temp
    print(data)


def select_sort(data):
    n = len(data)
    for i in range(n):
        min = data[i]
        for j in range(i, n):
            if data[j] < min:
                min = data[j]
                data[j], data[i] = data[i], data[j]
    print(data)

def count_sort(data):
    max = data[0]
    min = data[0]
    for num in data:
        if num > max:
            max = num
        if num < min:
            min = num
    if max == min:
        print(data)
    c = list()
    length = len(data)
    for i in range(max+1):
        c.append(0)
    for num in data:
        occurs = 0
        for i in range(length):
            if num == data[i]:
                occurs += 1
        c[num] = occurs
    for index,value in enumerate(c):
        while(value > 0):
            print(index)
            value -= 1

def insert_search(data, value, low, high):
    mid = low + (value -data[low])/(data[high] - data[low]) * (high - low)
    if data[mid] == value:
        return mid
    if (data[mid] > value):
        return insert_search(data, value, low, mid-1)
    if (data[mid] < value):
        return insert_search(data, value, mid+1, high)

def binary_search(data, value, low, high):
    mid = (low + high)//2
    if data[mid] == value:
        return mid
    elif data[mid] < value:
        return binary_search(data, value, mid+1, high)
    else:
        return binary_search(data, value, low, mid-1)

   
#维护堆的性质
#li 输入数组
#root 堆的根节点位置
#end 堆的最后一个元素的位置
def heapify2(li, root, end):
    lchild = 2 * root + 1
    while lchild <= end:
        if lchild + 1 <= end and li[lchild] < li[lchild + 1]:
            lchild = lchild + 1
        if li[root] < li[lchild]:
            li[root], li[lchild] = li[lchild] , li[root]
            root = lchild
            lchild = 2 * root + 1
        else:
            break

def heap_sort2(li):
    n = len(li)
    for i in range((n-1)//2 , -1, -1):
        heapify(li, i, len(li)-1)   # build the heap
    for i in range(n-1, 0, -1):
        li[0], li[i] = li[i], li[0]
        print("No {} bigger is {}".format(n-i, li[i]))
        heapify(li, 0, i-1)
    print(li)

def heapify(li, root, end):
    lchild = 2 * root + 1
    rchild = lchild + 1
    while lchild <= end:
        if rchild <= end and li[lchild] < li[rchild] :
            lchild = rchild
        if li[root] < li[lchild]:
            li[root], li[lchild] = li[lchild], li[root]
            root = lchild
            lchild = 2 * root + 1
        else:
            break

def heap_sort(li):
    n = len(li)
    for i in range((n-1)//2, -1, -1):
        heapify(li, i, n-1)
    for i in range(n-1, 0, -1):
        li[0],li[i] = li[i], li[0]
        print("No {} bigger is {}".format(n-i, li[i]))
        heapify(li, 0, i-1)
    print(li)


if __name__=="__main__":
    the_list = [6,2,3,8,0,1,9,7]
    #bubble_sort(the_list)
    #insert_sort(the_list)
    #select_sort(the_list)
    #count_sort(the_list)
    #print(insert_search(the_list, 7, 0, 7))
    print(heap_sort(the_list))


