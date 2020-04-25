"""
Merge sort algorithm
"""

def merge(arr1,arr2):
    """
    receives two sorted arrays and combines them (in sorted order)
    :param arr1: sorted array
    :param arr2: sorted array
    :return: sorted array
    """
    i = 0
    j = 0
    new_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_list.append(arr1[i])
            i += 1
        else:
            new_list.append(arr2[j])
            j += 1
    if i == len(arr1):
        new_list.extend(arr2[j:])
    if j == len(arr2):
        new_list.extend(arr1[i:])
    return new_list

def merge_sort(arr):
    """
    takes unsorted array and recurses on itself to sort it
    :param arr: unsorted array of integers
    :return: sorted array
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def main():
    arr = [3,5,2,8,6,7,10,22,13,16,12,1,4]
    print(merge_sort(arr))

if __name__ == "__main__":
    main()
