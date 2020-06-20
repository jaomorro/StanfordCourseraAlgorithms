"""
Bellman-Ford implementation of shortest path algortihm
Given a graph it finds the shortest path to each vertice from a source vertice
"""


def read_data(filename):
    """
    :param filename: filename of data
    :return: adjancy list
    """
    with open(filename) as f:
        data = f.read().strip("\n").split("\n")
    data_dict = {}
    for i in range(1,len(data)):
        vals = data[i].strip("\n").split(" ")
        data_dict.setdefault(int(vals[0]),{})
        data_dict[int(vals[0])][int(vals[1])] = int(vals[2])
    return data_dict

def bellman_ford(g,source):
    """
    Bellman-Ford algorithm to find shortest path from source to each vertice

    :param g : graph with distances between nodes
    :param source : source of the graph
    :return: dictionary with shortest path distance from source to each vertice
    """
    dist = {node: float('inf') for node in g}
    dist[source] = 0

    for i in range(len(g)-1):
        for node in g:
            for neighbor in g[node]:
                if dist[neighbor] > dist[node] + g[node][neighbor]:
                    dist[neighbor] = dist[node] + g[node][neighbor]

    for node in g:
        for neighbor in g[node]:
            if dist[neighbor] > dist[node] + g[node][neighbor]:
                return "Negative weight cycle"

    return dist

if __name__ == "__main__":
    filename = "Data/FW1.txt"
    graph = read_data(filename)

    distance = bellman_ford(graph,1)
    print(distance)

    # graph = {
    #     'a': {'c': 3},
    #     'b': {'a': 2},
    #     'c': {'b': 7, 'd': 1},
    #     'd': {'a': 6},
    # }
