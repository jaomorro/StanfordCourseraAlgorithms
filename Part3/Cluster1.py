"""
Your task in this problem is to run the clustering algorithm from lecture on this data set,
where the target number kk of clusters is set to 4. What is the maximum spacing of a 4-clustering?
Maximum spacing is the min distance between points in diff clusters when you are at desired
    cluster count
"""

import requests

def load_data(file_name):
    """
    load data to be used into a file
    :param file_name: file to load the data to
    :return: no returned data
    """

    url = "https://d18ky98rnyall9.cloudfront.net/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt?Expires=1588377600&Signature=EyYCj-UoIcf2XLkFGiXSINuf1M9B13qANb8oxJtvVg8zha~924m08Ck-lMZiI06pxtTpk1iaxYcifjR0~GaS6RIhwPEzUatBuGwphxL~vqjIU-1FsqlFII-HWMJJGOF-u5HE~UnnuPw-hIGitWjxVfiapu61MHI4aDpoFv3wcPQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    r = requests.get(url)
    data = r.text
    with open(file_name,"w") as f:
        f.write(data.strip("\n"))

def retrieve_data(filename):
    """
    load data from file into list
    :param file_name: name of the file where the data is stored
    :return: list of numbers
    """

    with open(filename) as f:
        data = f.read().strip("\n").split("\n")
    data_list = []
    for i in data[1:]:
        vals = i.split(" ")
        # weight, vert1, vert2
        data_list.append((int(vals[2]),int(vals[0]),int(vals[1])))
    data_list.sort()
    return data_list

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

if __name__ == "__main__":
    # desired number of clusters
    k_clusters = 4

    edges = retrieve_data("Data/Cluster1Data.txt")
    vert_1 = set([x[1] for x in edges])
    vert2 = set([x[2] for x in edges])
    vertices = vert_1.union(vert2) #distinct list of vertices

    # initialize parent and rank dictionaries
    parent = {node: node for node in vertices}
    rank = {node: 0 for node in vertices}

    # initialize cluster_cnt to the number of vertices
    # will count down each union until we reach the desired K
    cluster_cnt = len(vertices)
    # loop through each vertice
    for weight,vert1,vert2 in edges:
        if find(vert1,parent) != find(vert2,parent) and cluster_cnt == k_clusters:
            # when you are at the desired cluster cnt and vertices are in diff clusters
            # and would require a union
            # print result and break
            print(f"Max K spacing = {weight}")
            break
        if find(vert1,parent) != find(vert2,parent):
            parent,rank = union(vert1,vert2,parent,rank)
            cluster_cnt -= 1
