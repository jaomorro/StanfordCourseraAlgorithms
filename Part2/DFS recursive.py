"""
Depth first search recursive algorithm
"""

def dfs_recursive(g,v,explored):
    """

    :param g: graph as adjacency list
    :param v: starting vertex
    :return: list with all the points reachable from v
    """
    if v not in explored:
        explored.append(v)
        for i in g[v]:
            if i not in explored:
                dfs_recursive(g,i,explored)
    return explored

def main():
    g = [
        [1,2],
        [0,2,3],
        [0,1,3,5],
        [1,2,4,5],
        [3,6],
        [2,3,6],
        [4,5,7],
        [8,9],
        [7],
        [7]
    ]

    print(dfs_recursive(g,0,[]))

if __name__ == "__main__":
    main()


