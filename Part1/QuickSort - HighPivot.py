"""
Sort array using quicksort with a high pivot
"""

def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def main():
    arr = [5,2,4,1,3,8,7,6]
    quicksort(arr,0,len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
