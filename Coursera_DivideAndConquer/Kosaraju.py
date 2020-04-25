"""
Kosaraju algorithm computes the strongly connected components of a graph
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(5000000)

def dfs_topo(g):
    """
    Loops through vertices in graph
    :param g: adjacency list graph
    :return: topographically sorted list of vertices
    """
    explored = []
    stack = []
    for v in sorted(list(g.keys())):
        result = dfs_topo_sort(g,v,explored,stack)
    return result

def dfs_topo_sort(g,v,explored,stack):
    """
    searhes vertices on other end of edge for vertex passed in
    :param g: adjacency list graph
    :param v: vertex
    :param explored: list of vertices that have already been explored
    :param stack: topographically sorted list of vertices
    :return: topographically sorted list of vertices
    """
    explored.append(v)
    for i in g[v]:
        if i not in explored:
            dfs_topo_sort(g,i,explored,stack)
    if v not in stack:
        stack.insert(0,v)
    return stack

def dff_scc_group(g,v,explored,num_scc,result):
    """
    groups strongly connected components
    :param g: adjacency list graph
    :param v: vertex
    :param explored: list of vertices that have already been explored
    :param num_scc: scc group
    :param result: dictionary with scc groups
    :return: dictionary of scc groups
    """
    explored.append(v)
    for i in g[v]:
        if i not in explored:
            result[num_scc].append(i)
            dff_scc_group(g,i,explored,num_scc,result)
    return result

def dfs_scc(g,verts):
    """
    loops through vertices of reversed graph in order to capture scc
    :param g: adjacency list graph
    :param verts: list of vertices
    :return: dictionary of strongly connected components
    """
    explored = []
    num_scc = 0
    result = defaultdict(list)
    for v in verts:
        if v not in explored:
            num_scc += 1
            result[num_scc].append(v)
            dff_scc_group(g,v,explored,num_scc,result)
    return dict(result)

def rev_graph(g):
    """
    reverses a graph
    :param g: adjacency list graph
    :return: adjacency list of graph that is the reverse of the one passed in
    """
    g_rev = defaultdict(list)
    for k,v in g.items():
        if k not in g_rev.keys():
            g_rev[k] = []
        for num in v:
            g_rev[num].append(k)
    return dict(g_rev)

def read_graph_data(file_name):
    """
    read data from file and output adjecency list
    only use this if data is provided in file with one edge on each line
    :param file_name: location of the file
    :return: adjacency list
    """
    with open(file_name,"r") as f:
        data = f.readlines()

    d = defaultdict(list)
    for i in data:
        new_data = i.strip("\n").split(" ")
        d[new_data[0]].append(new_data[1])
    return d

g = {
    1: [5],
    2: [9],
    3: [1],
    4: [2,9],
    5: [3],
    6: [8,11],
    7: [4,5],
    8: [9,10,11],
    9: [5,7],
    10: [2,6],
    11: [3]
}

g = read_graph_data("C:\\Users\\Jimmy\\Desktop\\Misc\\KosarajuData.txt")
print("here")
#print(g)
r_graph = rev_graph(g)
#print(r_graph)
print("done with reverse")
verts_for_second_pass = dfs_topo(r_graph)
print(f"verts_for_second_pass = {verts_for_second_pass}")
scc = dfs_scc(g,verts_for_second_pass)
print(f"Strongly Connected Components = {scc}")


