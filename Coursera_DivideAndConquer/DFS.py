
# Iterative dfs algorithm that returns all vertexes reachable from v
def dfs_iterative(g,v):
    explored = []
    stack = [v]
    while len(stack) > 0:
        vert = stack.pop()
        print(f"vert = {vert} explored = {explored}")
        if vert not in explored:
            explored.append(vert)
            for i in g[vert]:
                if i not in explored:
                    stack.append(i)
    return explored

# Recursive dfs algorithm that returns all vertexes reachable from v
def dfs_recursive(g,v,explored):
    print(f"v = {v} explored = {explored}")
    if v not in explored:
        explored.append(v)
        for i in g[v]:
            print(F"i = {i}")
            if i not in explored:
                dfs_recursive(g,i,explored)
    return explored

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
print(dfs_recursive(g,0,[]))
