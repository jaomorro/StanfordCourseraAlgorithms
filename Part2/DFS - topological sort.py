"""
dfs topological sort
topological ordering of directed graphs assigns distinct #s to vertices with every edge traveling
    from a smaller # to larger one
Only DAGs can have a topological ordering
"""

def dfs_topo(g):
    """
    loops through graph keys and calls topo sort
    :param g: adjacency list graph
    :return: list of graph sorted topographically
    """
    explored = []
    stack = []
    for vert in g.keys():
        result = dfs_topo_sort(g,vert,explored,stack)
    return result

def dfs_topo_sort(g,v,explored,stack):
    """
    performs dfs topographical sort
    :param g: adjacency list graph
    :param v: starting vertex
    :param explored: list of explored vertexes
    :param stack: LIFO stack that keeps track of vertexes traversed
    :return: LIFO stack
    """
    explored.append(v)
    for i in g[v]:
        if i not in explored:
            dfs_topo_sort(g,i,explored,stack)
    if v not in stack:
        stack.insert(0,v)
    return stack

def main():
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

    print(g)
    print(dfs_topo(g))

if __name__ == "__main__":
    main()

