"""
Kruskal algorithm using Union Find implementation
"""

def graph_edges(g):
    """
    formats the graph into a list with structure [weight,vert1,vert2]

    :param g: adjanceny list graph
    :return: list sorted by weight (least to most)
    """
    edges = []
    for k,v in g.items():
        for dst,weight in v.items():
            # weight, source, destination
            edges.append([weight,k,dst])
    edges.sort()
    return edges

def find(vert,parent):
    """
    recursively calls the vertice until it finds the root
    root is when a vertice is its own parent

    :param vert: vertice you want to find the root of
    :param parent: dictionary with parent for each vertice
    :return: root of the vertice
    """
    if parent[vert] != vert:
        parent[vert] = find(parent[vert],parent)
    return parent[vert]

def union(vert1,vert2,parent,rank):
    """
    updates parent with a new root for one of the vertices (which ever one has the smaller rank)

    :param vert1: first vertice of edge
    :param vert2: second vertice of edge
    :param parent: dictionary with parent for each vertice
    :param rank: dictionary with rank of each vertice
    :return: parent, rank
    """
    vert1_p = find(vert1,parent)
    vert2_p = find(vert2,parent)
    if rank[vert1_p] >= rank[vert2_p]:
        parent[vert2_p] = vert1_p
        rank[vert1_p] += 1 if rank[vert2_p] == 0 else rank[vert2_p]
    else:
        parent[vert1_p] = vert2_p
        rank[vert2] += 1 if rank[vert1_p] == 0 else rank[vert1_p]
    return parent,rank

if __name__ == "__main__":
    g = {
        1: {2:2,3:4},
        2: {1:2,3:3,4:6},
        3: {1:4,2:3,4:5,5:1},
        4: {2:6,3:5,5:7},
        5: {3:1,4:7}
    }

    edges = graph_edges(g)
    mst = []
    vertices = list(g.keys())

    # initialize parent and rank dictionaries
    parent = {node: node for node in vertices}
    rank = {node: 0 for node in vertices}

    # loop through each vertivec
    for weight,vert1,vert2 in edges:
        if find(vert1,parent) != find(vert2,parent):
            parent,rank = union(vert1,vert2,parent,rank)
            mst.append([weight,vert1,vert2])

    print(f"mst = {mst}")
