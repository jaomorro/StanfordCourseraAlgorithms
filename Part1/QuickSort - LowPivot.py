"""
Sort array using quicksort with a low pivot
"""

def partition(arr,low,high):
    i = low+1
    pivot = arr[low]
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
    arr = [5,2,4,1,3,8,7,6]
    quicksort(arr,0,len(arr))
    print(arr)

if __name__ == "__main__":
    main()
