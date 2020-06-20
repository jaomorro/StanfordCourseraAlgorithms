"""
Kosaruja's algorithm is used to find the s trongly connected components of a graph

1. Perform dfs
2. Reverse the graph
3. Perform dfs on reversed graph
"""

from collections import defaultdict

def dfs_sort(g,v,explored,stack):
    """
    performs dfs
    :param g: adjacency list graph
    :param v: starting vertex
    :param explored: list of explored vertexes
    :param stack: LIFO stack that keeps track of vertexes traversed
    :return: LIFO stack
    """
    explored[v] = True
    for i in g[v]:
        if not explored[i]:
            dfs_sort(g,i,explored,stack)
    stack.append(v)
    return stack

def reverse_graph(g):
    """
    reverses a directed graph

    :param g: adjaceny list graph
    :return: adjacency list graph in reverse order
    """
    g_rev = defaultdict(list)
    for k in g:
        g_rev.setdefault(k, [])
        for vert in g[k]:
            g_rev[vert].append(k)
    return g_rev

def dfs_scc(g,v,explored,scc):
    """
    dfs that captures strongly connected components

    :param g: adjacency list graph
    :param v: starting vertex
    :param explored: list of explored vertexes
    :param scc: list of vertices in the scc
    :return : list of vertices in the scc
    """

    explored[v] = True
    scc.append(v)
    for vert in g[v]:
        if explored[vert] == False:
            dfs_scc(g,vert,explored,scc)
    return scc

def scc(g):
    """
    finds the scc of a graph

    :param g: adjacency list graph
    :return : dict of scc
    """
    explored = [False for x in range(max(list(g.keys()))+1)]
    stack = []

    # loop through vertices in graph with dfs to find stack
    for vert in g.keys():
        if not explored[vert]:
            dfs_sort(g,vert,explored,stack)

    # reverse the graph
    g_rev = reverse_graph(g)

    explored = [False for x in range(max(list(g.keys()))+1)]
    scc_num = 0
    scc_list = {}

    # dfs on the reversed graph to get the SCC
    while stack:
        i = stack.pop()
        if explored[i] == False:
            scc_num += 1
            scc_list[scc_num] = dfs_scc(g_rev,i,explored,[])

    return scc_list

if __name__ == "__main__":
    # g = {0: [1], 1: [2], 2: [3, 4], 3: [0], 4: [5], 5: [6], 6: [4, 7], 7: []}
    g = {0: [4], 1: [8], 2: [0], 3: [1, 8], 4: [2], 5: [7, 10], 6: [3, 4], 7: [8, 9, 10], 8: [4, 6], 9: [1, 5], 10: [2]}

    print(f"scc = {scc(g)}")




