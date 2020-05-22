"""
The distance between two nodes uu and vv in this problem is defined as the Hamming distance---
the number of differing bits --- between the two nodes' labels. For example, the Hamming distance
between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3
(since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of kk such that there is a kk-clustering with spacing at least 3?
That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split
into different clusters?
"""

import requests
from collections import defaultdict
from time import time


def find(vert,parent):
    """
    recursively calls the vertice until it finds the root
    root is when a vertice is its own parent

    :param vert: vertice you want to find the root of
    :param parent: dictionary with parent for each vertice
    :return: root of the vertice
    """
    if parent[vert] != vert:
        parent[vert] = find(parent[vert],parent)
    return parent[vert]

def union(vert1,vert2,parent,rank):
    """
    updates parent with a new root for one of the vertices (which ever one has the smaller rank)

    :param vert1: first vertice of edge
    :param vert2: second vertice of edge
    :param parent: dictionary with parent for each vertice
    :param rank: dictionary with rank of each vertice
    :return: parent, rank
    """
    vert1_p = find(vert1,parent)
    vert2_p = find(vert2,parent)
    if rank[vert1_p] >= rank[vert2_p]:
        parent[vert2_p] = vert1_p
        rank[vert1_p] += 1 if rank[vert2_p] == 0 else rank[vert2_p]
    else:
        parent[vert1_p] = vert2_p
        rank[vert2] += 1 if rank[vert1_p] == 0 else rank[vert1_p]
    return parent,rank

def retrieve_data(filename):
    with open(filename) as f:
        data = f.read()
    data_list = data.strip("\n").split("\n")
    return data_list[1:]

if __name__ == "__main__":
    data_list = retrieve_data("Data/ClusterLarge.txt")
    start_time = time() # track how long the job takes

    # create dict and hamming dist dict
    d = defaultdict(list) # dict of {binary int : index}
    ham1 = defaultdict(list) # dict of {index : list of nums with hamming dist 1 from number at index}
    ham2 = defaultdict(set) # dict of {index : list of nums with hamming dist 2 from number at index}
    data_nums = [] # list of binary ints

    # loop through all the records in the file
    for i in range(len(data_list)):
        bit_num = data_list[i].replace(" ","") # parse out the data to get the bit_num
        num = int(bit_num.replace(" ", ""), 2) # convert bit to a num
        #data_nums.append(int(bit_num,2)) #
        data_nums.append(num) # append num to list
        d[num].append(i) # add num and index to dict
        bit_num_original = list(bit_num) # create list of the bits 1/0s

        # loop through all the 1/0s in the bit so we can get the hamming dist 1 and 2
        # there is definitely a better way to do this but I am doing a double loop to
        #   outer loop alters each integer for hamming distance 1
        #   innser loop alters another integer then for hamming distance 2
        for j in range(len(bit_num)):
            bit_num_list = list(bit_num)
            if bit_num[j] == '0':
                bit_num_list[j] = '1'
            else:
                bit_num_list[j] = '0'
            bit_num_new = "".join(bit_num_list)
            num = int(bit_num_new, 2)
            ham1[i].append(num) # append new num for hamming dist 1
            # inner loop to get nums for hamming dist 2
            for l in range(len(bit_num_list)):
                if l != j:
                    if bit_num[l] == '0':
                        bit_num_list[l] = '1'
                    else:
                        bit_num_list[l] = '0'

                    bit_num_new = "".join(bit_num_list)
                    num = int(bit_num_new, 2)
                    ham2[i].add(num) # append num for hamming dist 2
                    bit_num_list[l] = bit_num_original[l]

    print(time() - start_time)
    print(f"len dict = {len(d)}")

    # create parent and rank dict
    parent = {node: node for node in range(len(data_list))}
    rank = {node: 0 for node in range(len(data_list))}

    # loop through dict to find records with hamming distance 0
    # these will be records that had identical bit nums and hence have
    #   multiple index records in key list
    cluster_cnt = len(parent)
    for k,v in d.items():
        if len(v) > 1:
            for j in range(len(v)-1):
                vert1 = v[j]
                vert2 = v[j+1]
                if find(vert1, parent) != find(vert2, parent):
                    parent, rank = union(vert1, vert2, parent, rank)
                    cluster_cnt -= 1

    print(f"cluster_cnt ham0 = {cluster_cnt}")
    print(time() - start_time)

    # loop through dict to find records with hamming distance 1
    # if a number in the list of values is a key in the dict then these records
    #   have a hamming dist 1 and need to be unioned
    for k,v in ham1.items():
        for ham1_record in v:
            ham1_vectors = d.get(ham1_record,-1)
            if ham1_vectors != -1:
                for ham1_vect in ham1_vectors:
                    vert1 = k
                    vert2 = ham1_vect
                    if find(vert1, parent) != find(vert2, parent):
                        parent, rank = union(vert1, vert2, parent, rank)
                        cluster_cnt -= 1

    print(f"cluster_cnt ham1 = {cluster_cnt}")
    print(time() - start_time)


    # loop through dict to find records with hamming distance 2
    # if a number in the list of values is a key in the dict then these records
    #   have a hamming dist 2 and need to be unioned
    for k,v in ham2.items():
        for ham2_record in v:
            ham2_vectors = d.get(ham2_record,-1)
            if ham2_vectors != -1:
                for ham2_vect in ham2_vectors:
                    vert1 = k
                    vert2 = ham2_vect
                    if find(vert1, parent) != find(vert2, parent):
                        parent, rank = union(vert1, vert2, parent, rank)
                        cluster_cnt -= 1

    print(f"cluster_cnt ham2 = {cluster_cnt}")
    print(time() - start_time)

    print(f"largest k = {cluster_cnt}")
