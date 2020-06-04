# TO-DO: Complete the selection_sort() function below
def selection_sort (arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[current_index]
        arr[current_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


'''
selection_sort - Version 2 
'''
def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort2(arr):
    result = []
    for i in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        result.append(arr.pop(smallest_index))

    return result

# r = selection_sort([1,9,5,4,2])
# print(r)
#


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # compare to your neighbor, if you are taller, swap
    flag_dirty = True
    while flag_dirty:
        flag_dirty = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                flag_dirty = True

    return arr

'''
STRETCH: implement the Count Sort function below
Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).
Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 
What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr