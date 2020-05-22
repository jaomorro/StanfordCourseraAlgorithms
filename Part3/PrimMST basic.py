"""
Straightforward implementation of Prim's Minimum Spanning Tree algorithm
"""

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

def prim_plain(g,v):
    """
    straightforward implementation of Prim's Minimum Spanning Tree algorithm
    :param g: adjency list of the graph
    :param start: starting point of graph
    :return: edges of MST with distance
    """
    unvisitied = {node: None for node in g}
    current = v
    curr_dist = 0
    unvisitied[current] = (curr_dist,current)  #distance, vector
    visit_path = {}

    while True:
        for neighbor, distance in g[current].items():
            if neighbor not in unvisitied:
                continue
            if unvisitied[neighbor] is None or distance < unvisitied[neighbor][0]:
                unvisitied[neighbor] = (distance,current)
        # do not insert into visit path during first loop
        if current != v:
            # key for visit path is (prior vertex, current vertex)
            visit_path[(unvisitied[current][1]),current] = unvisitied[current][0]
        del unvisitied[current]
        if not unvisitied:
            break
        candidates = [node for node in unvisitied.items() if node[1] is not None]
        prior_visited = current
        current, curr_dist = sorted(candidates, key=lambda x: x[1])[0]
    return visit_path

def main():
    filename = "Data/PrimMSTData.txt"
    g = read_data(filename)

    results = prim_plain(g,1)
    results_dist = sum(results.values())
    print(f"Prim MST basic = {results}")
    print(f"Prim MST basic distance = {results_dist}")

if __name__ == "__main__":
    main()

