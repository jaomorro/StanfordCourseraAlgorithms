"""
Run Dijkstra's algorithm and return the shortest-path distances to the following
ten vertices, in order: 7,37,59,82,99,115,133,165,188,197
"""

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


def dijkstra_algo(g,start):
    """
    Dijkstra's shortest path algorithm
    :param g: adjency list of the graph
    :param start: starting point of graph / the point you are finding distances from
    :return: dictionary with shortest path to each point
    """
    visited = {}
    unvisited = {node: None for node in g}
    current = start
    curr_dist = 0
    unvisited[current] = curr_dist

    while True:
        for neighbor, distance in g[current].items():
            if neighbor not in unvisited:
                continue
            new_dist = curr_dist + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > new_dist:
                unvisited[neighbor] = new_dist
        visited[current] = curr_dist
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1] is not None]
        current, curr_dist = sorted(candidates, key = lambda x: x[1])[0]
    return visited


def main():
    file = "Data/DijkstraData.txt"
    adj_list = load_graph(file)
    dij_output = dijkstra_algo(adj_list,1)

    # for class I need to find the shortest path to these points
    result = [node for node in dij_output.items() if node[0] in (7,37,59,82,99,115,133,165,188,197)]
    output = sorted(result,key=lambda x:x[0])
    output_set = [x[1] for x in output]
    print(output_set)

if __name__ == "__main__":
    main()



