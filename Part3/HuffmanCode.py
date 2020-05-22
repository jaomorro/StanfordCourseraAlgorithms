"""
Your task in this problem is to run the Huffman coding algorithm from lecture on this data set.
What is the min and max length of a codeword in the resulting Huffman code?
    By min/max length we mean the min/max length of the code for a given character
"""

import heapq
from collections import defaultdict


def load_data(filename):
    """
     load data to be used into a file

     :param file_name: file to load the data to
     :return: list of data
     """

    with open(filename) as f:
        data = f.read().strip("\n").split("\n")
        data = [int(x) for x in data]
    return data


def encode(freq):
    """
     Takes a dictionary of characters and weights (frequency of char in data) and applies
        a non prefix code to each character
     Heap data structure is used and code is applied using a binary tree format

     :param freq: dictionary with character as key and its frequency as value
     :return: list of lists where inner lists are [character, code] and outer list
                is ordered by length of code, character
     """

    heap = [[weight, [char, '']] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for rec in low[1:]:
            rec[1] = '0' + rec[1]
        for rec in high[1:]:
            rec[1] = '1' + rec[1]
        new_rec = [low[0] + high[0]] + low[1:] + high[1:]
        heapq.heappush(heap, new_rec)
    return sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x))


if __name__ == "__main__":
    data = load_data(("Data/HuffmanData.txt"))
    freq = defaultdict(int)
    for i in range(len(data)):
        freq[i] = data[i]

    result = encode(freq)
    print(result)
    print(f"min code len = {len(result[0][1])}")
    print(f"max code len = {len(result[-1][1])}")
