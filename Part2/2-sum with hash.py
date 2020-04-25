"""
Your task is to compute the number of target values tt in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,yx,y in the input file that satisfy x+y=tx+y=t.
"""

import requests
import json

def load_data(file_name):
    """
    load data to be used into a file
    :param file_name: file to load the data to
    :return: no returned data
    """
    url = "https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1587772800&Signature=KBufMS4gc7o4tCtPD1ndyUNsfeFuEBOtc1H1T7e63rw9E3XfZZAkMhPefegM7SVcUdhy~z~Yfj56cGXjd2fupteT8AYzsNFn87i5QDM9nqo2PdfwhzAc6AT1R6mXeSOk3S9Ip14ePN~FDsarkPP3-A0L2jCCf-948yybTVuPpX8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    r = requests.get(url)
    data = r.text
    with open(file_name,"w") as f:
        f.write(data.strip("\n"))

def retrieve_data(file_name):
    """
    load data from file into list
    :param file_name: name of the file where the data is stored
    :return: list of numbers
    """
    with open(file_name) as f:
        data = f.readlines()
    data_list = [int(x.strip("\n")) for x in data]
    return data_list

def target_nums(data,target_range):
    """

    :param data: list of numbers
    :param target_range: min and max of target range
    :return: number of target values in range that numbers summed to
    """
    min_range,max_range = target_range[0],target_range[1]
    target_nums = {}
    d = {}
    data.sort()
    i,j = 0,len(data)-1
    while i < j:
        num1 = data[i]
        num2 = data[j]
        if num1 == num2:
            i += 1
        elif num1 + num2 >= min_range and num1 + num2 <= max_range:
            target_nums.setdefault(num1+num2,0)
            i += 1
        elif num1 + num2 < min_range:
            i += 1
        elif num1 + num2 > max_range:
            j -= 1

    return len(target_nums)

def main():
    file_name = "HashData.txt"
    data = retrieve_data(file_name)
    result = target_nums(data,[-10000,10000])
    print(f"result = {result}")

if __name__ == "__main__":
    main()
