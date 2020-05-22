"""
Implementation of Prim's Minimum Spanning Tree algorithm using heap
"""

import heapq

def read_data(filename):
    d = {}
    with open(filename) as f:
        data = f.read().strip("\n").split("\n")[1:]
    for i in data:
        records = i.split(" ")
        vect1 = int(records[0])
        vect2 = int(records[1])
        dist = int(records[2])
        d.setdefault(vect1,{})
        d[vect1][vect2] = dist
        d.setdefault(vect2,{})
        d[vect2][vect1] = dist
    return d

def prim_heap(g,start):
    """
    heap implementation of Prim's Minimum Spanning Tree algorithm
    :param g: adjency list of the graph
    :param start: starting point of graph
    :return: edges of MST with distance
    """
    distances = {node: None for node in g}
    distances[start] = (0,start)
    visit_path = {}
    mst = set()

    pq = [(0,start)]
    while len(pq) > 0:
        curr_dist, current_vect = heapq.heappop(pq)
        if current_vect in mst:
            if current_vect == 1:
                print(distances)
            continue
        for neighbor,dist in g[current_vect].items():
            if neighbor in mst:
                continue
            if distances[neighbor] is None or dist < distances[neighbor][0]:
                distances[neighbor] = (dist,current_vect)
                heapq.heappush(pq,(distances[neighbor][0],neighbor))
        mst.add(current_vect)
    # format the result into dict of form {(vect1, vect2): dist}
    for k,v in distances.items():
        visit_path[(v[1],k)] = v[0]
    return visit_path


def main():
    filename = "Data/PrimMSTData.txt"
    g = read_data(filename)

    results_path = prim_heap(g,1)
    results_dist = sum(results_path.values())
    print(f"Prim MST heap path = {results_path}")
    print(f"Prim MST heap distance = {results_dist}")

if __name__ == "__main__":
    main()

