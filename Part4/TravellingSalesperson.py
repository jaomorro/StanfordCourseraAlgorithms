"""
In this assignment you will implement one or more algorithms for the traveling salesman problem,
such as the dynamic programming algorithm covered in the video lectures.
The first line of the file indicates the number of cities. Each city is a point in the plane, and each subsequent
line indicates the x- and y-coordinates of a single city.
The distance between two cities is defined as the Euclidean distance
Find the minimum cost of a traveling salesman tour for this instance
"""

from itertools import combinations, permutations
from copy import copy
from collections import defaultdict
import math
import time

def read_data(filename):
    """
    Reads and organizes the data from file

    :param filename : file path to read data from
    :return : NxN matrix with distance between each set of vertices
    """

    with open(filename) as f:
        data = f.readlines()

    mat = [[0 for x in range(25)] for x in range(25)]
    for i in range(1,len(data)):
        vert1 = data[i].strip("\n").split(" ")
        for j in range(1,len(data)):
            vert2 = data[j].strip("\n").split(" ")
            dist = math.sqrt((float(vert1[0])-float(vert2[0]))**2 + (float(vert1[1])-float(vert2[1]))**2)
            mat[i - 1][j - 1] = dist
    return mat

def dist_func(perms, d_current, d_lookup):
    """
    Loop through all combinations at given step
    ex - (1,2), (1,3), (2,3) for step 3 with vertices (1,2,3)
    Finds the shortest path to each vertex in (1,2,3)

    :param perms : list of all combinations
    :param d_current : dict to capture distances to current step via each vertice in step
                        Empty dict passed in for all steps but second because third step needs
                        k,v from step one
    :param d_lookup : k,v distances from the prior step
    :return: dictionary with min dist to step via each node
    """

    for perm in perms:
        d_current[perm] = {}
        for h in range(len(perm)):
            head = perm[h]
            new_d = tuple(x for x in perm if x != head)
            new_dist = min(list([(d_lookup[new_d][x] + mat[x][head]) for x in d_lookup[new_d]]))
            d_current[perm][head] = new_dist
    return d_current


if __name__ == "__main__":
    mat = read_data("Data/TSP.txt")

    start_time = time.time()
    nums = list([i for i in range(1,len(mat))])

    # loop through all potential paths except the final stop back at starting vertex (vert 0 in this case)
    for i in range(1,len(mat)):
        print(f"i = {i}")
        perms = list(combinations(nums, i))
        print(len(perms))
        if i == 1:
            d_current = {}
            for perm in perms:
                d_current[perm] = {}
                d_current[perm][0] = mat[0][perm[0]]
        elif i == 2:
            d_current = dist_func(perms, d_current, d_current)
        elif i%2 == 0:
            d_current = dist_func(perms, {}, d_current)
        else:
            d_current = dist_func(perms, {}, d_current)
        print(f"{i} --- %s seconds --- % {(time.time() - start_time)}")

    # find the dist back to the starting vertex
    complete_list = tuple([x for x in range(len(mat))])
    dist_final = {}
    dist_final[complete_list] = {}
    final_perm = tuple([x for x in range(1,len(mat))])
    head = 0
    new_dist = min(list([(d_current[final_perm][x] + mat[x][head]) for x in d_current[final_perm]]))
    dist_final[complete_list][head] = new_dist

    print(f"dist_final = {dist_final[complete_list]}")
    print(f"{i} --- %s seconds --- % {(time.time() - start_time)}")
