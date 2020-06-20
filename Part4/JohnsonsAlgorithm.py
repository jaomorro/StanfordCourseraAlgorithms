"""
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which,
if any, of the three graphs have no negative cycles. For each such graph, you should compute
all-pairs shortest paths and remember the smallest one (i.e., compute \min_{u,v \in V} d(u,v)min
u,v∈V d(u,v), where d(u,v)d(u,v) denotes the shortest-path distance from uu to vv).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below.
If exactly one graph has no negative-cost cycles, then enter the length of its shortest
shortest path in the box below. If two or more of the graphs have no negative-cost cycles,
then enter the smallest of the lengths of their shortest shortest paths in the box below.
"""

import heapq

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
                return False
    return dist

def dijkstra_heap(graph,start):
    """

    :param graph: adjacency list graph
    :param start: starting vertex
    :return: dictionary with shortest distance to each vertex from starting vertex
    """
    visited = []
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0,start)]
    while len(pq) > 0:
        curr_dist, curr_vert = heapq.heappop(pq)
        if curr_dist > distances[curr_vert]:
            continue
        for neighbor, weight in graph[curr_vert].items():
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq,(new_dist,neighbor))
    return distances

def johnson(g):
    """
    run johnsons algorithm to reweight the graph and find shortest paths

    :param graph: adjacency list graph
    :return: graph with vertices and shortest path to every other vert in graph
    """

    # run bellman ford algo
    # this will find shortest path dist betyween the new vert and all existing verts
    # this is needed so we can re-weight the edges
    new_dist = bellman_ford(g, 'extra')
    if new_dist == False:
        # Negative weight set so return False
        return False
    else:
        del new_dist['extra']

        # re-weight the edges
        new_g = {}
        for node in g:
            if node != 'extra':
                new_g[node] = {}
                for neighbor in g[node]:
                    new_g[node][neighbor] = g[node][neighbor] + new_dist[node] - new_dist[neighbor]

        # create a dict to hold shortest path dist between every set of verts
        final_g = {}
        for k in new_g:
            final_g[k] = {}
            for i in new_g:
                final_g[k][i] = float('inf')

        # run dijkstras algo on every node
        # this will find shortest path betwwen node and every other node
        for k in new_g:
            result = dijkstra_heap(new_g, k)

            # reapply original weights to each edge
            for node in result:
                final_g[k][node] = result[node] - new_dist[k] + new_dist[node]

        return final_g

if __name__ == "__main__":

    min_val_set = False

    # loop through files
    data_files = ["Data/FW1.txt","Data/FW2.txt","Data/FW3.txt"]
    for file in data_files:
        #print(file)
        g = read_data(file)

        # add new vertice and give it weight of 0 to every existing vert
        g['extra'] = {}
        for k in g:
            g['extra'][k] = 0

        final_g = johnson(g)

        if final_g:
            if not min_val_set:
                min_val_set = True
                overall_min_val = 1000000
            # loop through k,v pairs to find the min shortest path
            for k,v in final_g.items():
                min_val = min(v.values())
                if min_val < overall_min_val:
                    overall_min_val = min_val

    print(f"overall_min_val = {overall_min_val if min_val_set else 'Negative weight cycles'}")