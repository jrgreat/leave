def bubble_sort(to_be_sort_list):
    if  not isinstance(to_be_sort_list, list):
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


if __name__=="__main__":
    the_list = [6,2,3,8,0,1,9,7]
    #bubble_sort(the_list)
    #insert_sort(the_list)
    #select_sort(the_list)
    count_sort(the_list)


