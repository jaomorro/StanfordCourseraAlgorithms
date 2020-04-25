"""
Breadth first search algorithm
"""

from collections import deque

def bfs(g,v):
    """

    :param g: graph as adjacency list
    :param v: starting vertex
    :return: list with two dictionaries
            parent : each vertex's parent (meaning the vertex used to get to it)
            dist : distance each vertex is from the starting vertex
    """
    dist = {v:0}
    parent = {v:None}
    l = 0
    q = deque()
    q.append(v)
    while len(q) > 0:
        vert = q[0]
        q.popleft()
        for i in g[vert]:
            if i not in parent.keys():
                q.append(i)
                parent[i] = vert
                dist[i] = dist[parent[i]] + 1
        l += 1
    return parent,dist

def main():
    g = [[1,2],
         [0,2,6],
         [0,1,3],
         [2,4,6,7],
         [3,5,7],
         [4],
         [1,3,7],
         [3,4,6]
         ]

    result = bfs(g,2)
    print(f"parent = {result[0]}")
    print(f"distances = {result[1]}")

if __name__ == "__main__":
    main()
