"""
Depth first search iterative algorithm
"""

def dfs_iterative(g,v):
    """

    :param g: graph as adjacency list
    :param v: starting vertex
    :return: list with all the points reachable from v
    """
    explored = []
    stack = [v]
    while len(stack) > 0:
        vert = stack.pop()
        if vert not in explored:
            explored.append(vert)
            for i in g[vert]:
                if i not in explored:
                    stack.append(i)
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

    print(dfs_iterative(g,0))

if __name__ == "__main__":
    main()
