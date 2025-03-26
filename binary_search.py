

def binary_search(nums, value):
    start = 0
    length = len(nums)
    end = length - 1
    while True:
        mid = int((start + end)/2)
        if nums[mid] == value:
            return mid
        if value < nums[mid]:
            end = mid -1
  
        if value > nums[mid]:
            start = mid + 1

        if start >= end:
            return 0 

def binary_search_recursive(nums, val, low, high):
    mid = (low + high)//2
    if nums[mid] == val:
        return mid
    if low >= high:
        return -1
    if nums[mid] < val:
        return binary_search_recursive(nums, val, mid+1, high)
    if nums[mid] > val:
        return binary_search_recursive(nums, val, low, high-1)



if __name__=="__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    #print(binary_search(nums, 11))
    print(binary_search_recursive(nums, 11, 0, len(nums)-1))