"""
Your task in this problem is to run the dynamic programming algorithm
(and the reconstruction procedure) from lecture on this data set.
The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones
belong to the maximum-weight independent set? (By "vertex 1" we mean the first
vertex of the graph---there is no vertex 0.) In the box below, enter a 8-bit string,
where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight
independent set, and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517
are in the maximum-weight independent set and the other four vertices are not,
then you should enter the string 10011010 in the box below.
"""

def load_data(filename):
    """
    load data from file

    :param filename: name of file
    :output: list of numbers from file
    """
    with open(filename) as f:
        data = f.read().strip("\n").split("\n")
        data = [int(x) for x in data]
    return data


def mwis(data):
    """
    find the Max Weight Independent Set

    :param data: list of numbers
    :output: list of weight along each step of MWIS
            list of indices that belong in set
    """

    arr = [None for x in range(len(data)+1)]
    arr[0] = 0
    arr[1] = data[0]
    for i in range(2,len(arr)):
        if arr[i-1] > (arr[i-2] + data[i-1]):
            arr[i] = arr[i-1]
        else:
            arr[i] = (arr[i-2] + data[i-1])

    vals = []
    i = len(arr)-1
    while i >= 1:
        if arr[i-1] > (arr[i-2] + data[i-1]):
            i -= 1
        else:
            vals.append(i-1)
            i -= 2
        if i == 0:
            vals.append(i)
    vals.sort()

    return arr, vals

if __name__ == "__main__":
    data = load_data("Data/MWISData.txt")
    weights, indices = mwis(data)

    # this is to answer the question from coursera class
    answer = []
    nums = [1, 2, 3, 4, 17, 117, 517, 997]
    for i in nums:
        if i-1 in indices:
            answer.append('1')
        else:
            answer.append('0')
    print(''.join(answer))
