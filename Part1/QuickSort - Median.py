"""
Sort array using quicksort with median-of-three as pivot
"""

# initializing counts
# this is purely for comparison purposes to count the # of pivots
count_pivot_median = 0

# Median-of-three method used to choose pivot element for sorting using Quick Sort
def middle_index(x):
    """ Returns the index of the middle element of an array """
    if len(x) % 2 == 0:
        middle_index = len(x)/2 - 1
    else:
        middle_index = len(x)/2
    return int(middle_index)

def median_index(x,i,j,k):
    """ Returns the median index of three when passed an array and indices of any 3 elements of that array """
    if (x[i]-x[j])*(x[i]-x[k]) < 0:
        return i
    elif (x[j]-x[i])*(x[j]-x[k]) < 0:
        return j
    else:
        return k

def countComparisonsMedianOfThree(x):
    """ Counts number of comparisons while using Quick Sort with median-of-three element is chosen as pivot """
    global count_pivot_median
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        count_pivot_median += len(x)-1
        k = median_index(x, 0, middle_index(x), -1)
        if k != 0: x[0], x[k] = x[k], x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = countComparisonsMedianOfThree(x[:i])
        second_part = countComparisonsMedianOfThree(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def main():
    numList = [4,3,7,1,2,8,11,12,13,15,22,77,54,69,78,123,42,90]
    arr = countComparisonsMedianOfThree(numList)
    print(count_pivot_median)
    print(arr)

if __name__ == "__main__":
    main()
