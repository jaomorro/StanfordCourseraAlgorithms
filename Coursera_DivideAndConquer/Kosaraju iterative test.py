from collections import defaultdict, deque

g = {
    1: [3],
    2: [4,10],
    3: [5,11],
    4: [7],
    5: [1,7,9],
    6: [10],
    7: [9],
    8: [6],
    9: [2,4,8],
    10: [8],
    11: [6,8]
}


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
        d[int(new_data[0])].append(int(new_data[1]))
    return d

num_nodes = len(g)
visited = [False] * num_nodes
stack = deque()
order = []
for node in range(1,num_nodes+1):
    print(node)
    print(visited)
    if visited[node-1] == False:
        stack.append(node)
    print(f"stack = {stack}")
    while stack:
        done = True
        for head in g[stack[0]]:
            print(f"head = {head} visited = {visited} stack = {stack}")
            if visited[head-1] == False:
                stack.append(head)
                visited[head-1] = True
                done = False
        if done:
            order.append(stack[0])
            del stack[0]

print(order)

