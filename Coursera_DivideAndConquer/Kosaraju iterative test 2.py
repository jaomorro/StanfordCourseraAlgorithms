from collections import deque, defaultdict
import copy

def topo_sort(g,vert,visit,visit_list,result):
    cnt = 0
    while True:
        print(f"cnt = {cnt}")
        if visit[vert] == "open":
            #print(f"vert = {vert} len = {len(g[vert])} vals = {g[vert]}")
            if len(g[vert]) > 0:
                i = 0
                while i < len(g[vert]):
                    val = g[vert][i]
                    #print(f"i = {i} val = {val}")
                    if val in visit_list or visit.get(val,"NA") == "closed":
                        #print(f"vert = {vert} g[vert] = {g[vert]}")
                        del g[vert][i]
                        #print(f"after del vert = {vert} g[vert] = {g[vert]}")
                    else:
                        i += 1
                if len(g[vert]) == 0:
                    while len(g[vert]) == 0:
                        result.append(vert)
                        visit[vert] = "closed"
                        visit_list.pop()
                        if len(visit_list) == 0:
                            #print(f"RESULT = {result}")
                            return result, visit
                        vert = visit_list[-1]
                        #print(f"result = {result}")
                else:
                    vert = g[vert].pop(0)
            else:
                while len(g[vert]) == 0:
                    result.append(vert)
                    visit[vert] = "closed"
                    visit_list.pop()
                    if len(visit_list) == 0:
                        #print(f"RESULT = {result}")
                        return result, visit
                    vert = visit_list[-1]
                    #print(f"result = {result}")
            if vert not in visit:
                visit[vert] = "open"
                visit_list.append(vert)
            #print(f"here: vert = {vert} visit_list = {visit_list} ")
            cnt += 1


def topo(g):
    visit = {}
    visit_list = []
    result = deque()
    g_copy = copy.deepcopy(g)
    for vert in g.keys():
        print(f"vert = {vert}")
        if visit.get(vert,"NA") != "closed":
            visit_list.append(vert)
            visit[vert] = 'open'
            #print(f"vert = {vert} visit = {visit} visit_list = {visit_list}")
            result, visit = topo_sort(g_copy,vert,visit,visit_list,result)
            #print(result)
    return result

def read_graph_data(file_name):
    """
    read data from file and output adjecency list
    only use this if data is provided in file with one edge on each line
    :param file_name: location of the file
    :return: adjacency list
    """
    with open(file_name,"r") as f:
        data = f.readlines()

    d = defaultdict(list)
    for i in data:
        new_data = i.strip("\n").split(" ")
        d[new_data[0]].append(new_data[1])
    return d


g = {
    1: [3],
    2: [4,10],
    3: [5,11],
    4: [7],
    5: [1,7,9],
    6: [10],
    7: [9],
    8: [6],
    9: [2,4,8],
    10: [8],
    11: [6,8]
}

g = read_graph_data("C:\\Users\\Jimmy\\Desktop\\Misc\\KosarajuData.txt")
#print(g)
print(topo(g))
