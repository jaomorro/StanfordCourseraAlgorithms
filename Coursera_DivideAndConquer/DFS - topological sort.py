"""
dfs topological sort
topological ordering of directed graphs assigns distinct #s to vertices with every edge traveling
    from a smaller # to larger one
Only DAGs can have a topological ordering
"""
def dfs_topo(g):
    explored = []
    stack = []
    for vert in g.keys():
        result = dfs_topo_sort(g,vert,explored,stack)
    return result

def dfs_topo_sort(g,v,explored,stack):
    explored.append(v)
    for i in g[v]:
        if i not in explored:
            dfs_topo_sort(g,i,explored,stack)
    if v not in stack:
        stack.insert(0,v)
    return stack

# g = {
#     's': ['v','w'],
#     'v': ['t'],
#     'w': ['t'],
#     't': []
# }

# g = {
#     1: [3],
#     2: [4,10],
#     3: [5,11],
#     4: [7],
#     5: [1,7,9],
#     6: [10],
#     7: [9],
#     8: [6],
#     9: [2,4,8],
#     10: [8],
#     11: [6,8]
# }

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



