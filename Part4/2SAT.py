"""
The file format is as follows. In each instance, the number of variables and the number of clauses is the same,
and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals,
with a number denoting the variable and a "-" sign denoting logical "not".

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable.
"""


from collections import  defaultdict
import sys
sys.path.insert(1,'../Part2')
import Kosaraju


def read_data(filename):
    """
    read data from file

    :param filename : file with data. First row is # records and subsequent rows are clauses specified by literals
    :return : number of records, list of arrays
    """

    with open(filename) as f:
        data = f.readlines()

        data_list = []
        nums_in_data = int(data[0].strip("\n"))
        for i in range(1,len(data)):
            num1 = int(data[i].strip("\n").split(" ")[0])
            num2 = int(data[i].strip("\n").split(" ")[1])
            data_list.append((num1, num2))
    return nums_in_data, data_list


def find_edges(nums_in_data, data_list):
    """
    creates edges for a graph by taking the literals provided
    Two edges are created for each array
        Negate the first # with the second as is
        Negate the second # with the first as is
    :param nums_in_data : number of records in data provided
    :param data_list : records provided
    :return : list of arrays of edges
    """

    edges = []
    for vert in data_list:
        num1b = vert[0] * -1
        if num1b < 0:
            num1b = (num1b * -1) + nums_in_data
        num2b = vert[1] * -1
        if (num2b) < 0:
            num2b = (num2b * -1) + nums_in_data
        num1a = vert[0]
        if num1a < 0:
            num1a = (num1a * -1) + nums_in_data
        num2a = vert[1]
        if num2a < 0:
            num2a = (num2a * -1) + nums_in_data

        edges.append((num1b-1, num2a-1))
        edges.append((num2b-1, num1a-1))
    return edges


def create_graph(edges):
    """
    create an adjacency list graph from edges
    :param edges : list of arrays of edges
    :return : adjacency list graph
    """
    graph = defaultdict(list)
    for vert in edges:
        graph[vert[0]].append(vert[1])

    missing = []
    for v in graph.values():
        for num in v:
            if graph.get(num, "NA") == "NA":
                missing.append(num)
    for num in missing:
        graph[num] = []
    return graph


if __name__ == "__main__":

    two_sat_complete_list = [False for x in range(6)]

    # loop through files provided
    for i in range(1,7):
        nums_in_data, data = read_data(f"Data/2SAT_Data{i}.txt")
        edges = find_edges(nums_in_data, data)
        graph = create_graph(edges)

        scc_list = Kosaraju.scc(graph)

        # loop through each scc to see if it contains an x and -x
        # if it does then it is no 2SAT complete
        two_sat_complete = True
        for k,v in scc_list.items():
            d = {}
            for num in v:
                if num >= nums_in_data:
                    num -= nums_in_data
                d.setdefault(num,0)
                if d[num] == 1:
                    two_sat_complete = False
                    break
                else:
                    d[num] += 1

        two_sat_complete_list[i-1] = two_sat_complete

    print(f"two_sat_complete = {two_sat_complete_list}")