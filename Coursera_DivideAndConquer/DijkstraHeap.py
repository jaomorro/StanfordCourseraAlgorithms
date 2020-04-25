import heapq

def load_graph(file):
    adj_list = {}
    with open(file) as f:
        for line in f:
            split_line = line.strip("\n").rstrip().split("\t")
            line_dict = {}
            for i in range(1,len(split_line)):
                val_list = split_line[i].split(",")
                line_dict[int(val_list[0])] = int(val_list[1])
            adj_list[int(split_line[0])] = line_dict
    return adj_list


def dijkstra_heap(graph,start):
    visited = []
    distances = {node: None for node in graph}
    distances[start] = 0

    pq = [(0,start)]
    while len(pq) > 0:
        curr_dist, curr_vert = heapq.heappop(pq)
        if curr_dist > distances[curr_vert]:
            continue
        for neighbor, weight in graph[curr_vert].items():
            new_dist = curr_dist + weight
            if distances[neighbor] is None or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq,(new_dist,neighbor))
    return distances


file = "C:\\Users\\Jimmy\\Desktop\\Misc\\DijkstraData.txt"
graph = load_graph(file)
result = dijkstra_heap(graph,1)
print(result)
