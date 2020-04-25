# rselect finds the ith largest number in an array

import random

def partition(arr,low,high):
    i = low + 1
    pivot_index = random.randint(low,high-1)
    arr[low],arr[pivot_index] = arr[pivot_index],arr[low]
    pivot = arr[low]
    for j in range(i,high):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[low], arr[i-1] = arr[i-1],arr[low]
    return i

def rselect(arr,ind):
    if len(arr) == 1:
        return arr[0]
    i = partition(arr,0,len(arr))
    if i == ind:
        return arr[i-1]
    elif i > ind:
        return rselect(arr[:i-1],ind)
    else: # i < ind
        ind -= i
        return rselect(arr[i:],ind)


arr = [4,3,7,1,2,8,11,12,13,15,22,77,54,69,78,123,42,90]
num = rselect(arr,7)
print(f"NUM = {num}")
print(arr)
