def bubble_sort(to_be_sort_list):
    if  not isinstance(to_be_sort_list, list):
        raise Exception("not a list!")
    n = len(to_be_sort_list)
    for i in range(n):
        for j in range(n-i-1):
            if to_be_sort_list[j] > to_be_sort_list[j+1]:
                to_be_sort_list[j], to_be_sort_list[j+1] = to_be_sort_list[j+1], to_be_sort_list[j]

    print(to_be_sort_list)


if __name__=="__main__":
    the_list = [6,2,3,8,0,1,9,7]
    bubble_sort(the_list)

