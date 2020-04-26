"""
Add numbers from list one by one, find the median, and then sum all the medians
"""
import heapq

def read_data(file_name):
    with open(file_name) as f:
        data = f.readlines()
        nums = [int(x.strip("\n")) for x in data]
    return nums

def find_median(nums):
    """
    loops through all nums in a list and finds the median as each new number is added
    :param nums: list of numbers
    :return: sum of the medians
    """
    h1 = []
    h2 = []
    heapq.heapify(h1)
    heapq.heapify(h2)

    for i in range(len(nums)):
        num = nums[i]
        if i == 0:
            heapq.heappush(h1,num*-1)
            median = (h1[0] * -1)
        else:
            if num < h1[0] * -1:
                heapq.heappush(h1,num*-1)
            else:
                heapq.heappush(h2,num)
            if len(h1) - len(h2) > 1:
                num_to_move = heapq.heappop(h1) * -1
                heapq.heappush(h2,num_to_move)
            elif len(h2) - len(h1) > 0:
                num_to_move = heapq.heappop(h2) * -1
                heapq.heappush(h1,num_to_move)
            median += (h1[0] * -1)
    return median

def main():
    file_name = "Data/HeapData.txt"
    nums = read_data(file_name)
    median = find_median(nums)
    print(median)
    print(median%10000)

if __name__ == "__main__":
    main()


