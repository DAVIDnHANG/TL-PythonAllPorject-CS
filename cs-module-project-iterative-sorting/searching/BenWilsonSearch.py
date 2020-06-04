def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # give us some initial values
    low = 0
    high = len(arr) - 1
    mid = 0

    # begin a loop
    while low <= high:

        # set our middle
        mid = (high + low) // 2

        # if the target is higher than the middle,
        # bring the low side up to beyond the middle
        if arr[mid] < target:
            low = mid + 1

        # if the target is lower than the mid,
        # bring the high down to below mid
        elif arr[mid] > target:
            high = mid - 1


        # if it is not higher or lower it is equal :D
        else:
            return mid


    return -1  # not found
