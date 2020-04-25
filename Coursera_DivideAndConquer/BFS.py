from collections import deque

def bfs(g,v):
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

g = [[1,2],
     [0,2,6],
     [0,1,3],
     [2,4,6,7],
     [3,5,7],
     [4],
     [1,3,7],
     [3,4,6]
     ]

print(bfs(g,2))
