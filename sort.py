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



if __name__=="__main__":
    the_list = [6,2,3,8,0,1,9,7]
    #bubble_sort(the_list)
    
    print(quick_sort(the_list))


