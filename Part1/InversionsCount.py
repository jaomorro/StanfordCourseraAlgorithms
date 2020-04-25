"""
Count the number of inversions in a given list of ints
piggybacks off of merge sort
"""

def merge(arr1,arr2,cnt):
    i = 0
    j = 0
    new_list = []
    inv_cnt = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_list.append(arr1[i])
            i += 1
        else:
            new_list.append(arr2[j])
            cnt += len(arr1[i:])
            j += 1
    if i == len(arr1):
        new_list.extend(arr2[j:])
    if j == len(arr2):
        new_list.extend(arr1[i:])
    return new_list,cnt

def merge_sort(arr,cnt):
    if len(arr) <= 1:
        return arr,0
    mid = len(arr) // 2
    left, left_cnt = merge_sort(arr[:mid],cnt)
    right, right_cnt = merge_sort(arr[mid:],cnt)
    new_arr, split_cnt = merge(left,right,cnt)
    inv_cnt = left_cnt + right_cnt + split_cnt
    return new_arr, inv_cnt

def main():
    arr = [6,5,4,3,2,1]
    ordered_arr, inv_cnt = merge_sort(arr,0)
    print(f"inv_cnt = {inv_cnt}")

if __name__ == "__main__":
    main()
