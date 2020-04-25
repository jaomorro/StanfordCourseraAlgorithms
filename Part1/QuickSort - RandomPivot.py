"""
Sort array using quicksort with a random pivot
"""

import random

# cnt_pivot is here to count the pivots used
# this is purely for comparison purposes to see how the # of pivots can change with each run
cnt_pivot = 0

def partition(arr,low,high):
    global cnt_pivot
    i = low+1
    pivot_index = random.randint(low,high-1)
    arr[low],arr[pivot_index] = arr[pivot_index],arr[low]
    pivot = arr[low]
    cnt_pivot += len(arr[low:high])-1
    for j in range(low+1,high):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[low],arr[i-1] = arr[i-1],arr[low]
    return i-1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi)
        quicksort(arr,pi+1,high)

def main():
    arr = [4,3,7,1,2,8,11,12,13,15,22,77,54,69,78,123,42,90]
    quicksort(arr,0,len(arr))
    print(arr)
    print(f"comparisons = {cnt_pivot}")

if __name__ == "__main__":
    main()
