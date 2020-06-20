"""
Floyd Warshall shortest paths algorithm
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


def floyd_warshall(graph):
    """
    uses floyd warshall algo to find shortest path between every set of points
    :param graph: adjancy list of edges and weights
    :return: matrix with shortest paths
    """

    g_len = len(graph)
    matrix = [[float('inf') for x in range(len(graph))] for x in range(len(graph))]

    for node in graph:
        for neigbor in graph[node]:
            matrix[node-1][neigbor-1] = graph[node][neigbor]
    for i in range(len(graph)):
        matrix[i][i] = 0

    for k in range(g_len):
        print(f"k = {k}")
        for i in range(g_len):
            for j in range(g_len):
                if matrix[i][j] > matrix[i][k] + matrix[j][k]:
                    matrix[i][j] = matrix[i][k] + matrix[j][k]

    for k in range(g_len):
        if matrix[k][k] < 0:
            return "Negative cycle"

    return matrix

if __name__ == "__main__":
    graph = read_data("Data/FW3.txt")
    result = floyd_warshall(graph)
    print(result)

