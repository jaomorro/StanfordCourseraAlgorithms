"""
Find max element in unimodal array
"""

def find_max_unimodal(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    mid = len(arr) // 2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid] > arr[mid-1]:
        return find_max_unimodal(arr[mid+1:])
    elif arr[mid] > arr[mid+1]:
        return find_max_unimodal(arr[:mid])

def main():
    arr = [1,2,3,5,6,8,9,11,13,15,17,22,23,24,25,26,27,45,66,67,7,4,0,-1,-2,-3,-4,-5]
    print(find_max_unimodal(arr))

if __name__ == "__main__":
    main()
