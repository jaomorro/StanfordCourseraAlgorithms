"""
Counts no. of crossing edges in the min cut of given undirected graph by contracting
randomly chosen edges with a success probability of i/n^2 which can be boosted to a better
1/n by repeated trails ((n^2)logn trails approx.)
"""


import random

FILE = "KargerMinCutData.txt"
ROUNDS = 200

def minCut(edges):
    while vertexes(edges) > 2:
        removeOne(edges)
    return len(edges)

def removeOne(edges):
    r = random.choice(edges)
    edges.remove(r)
    merge(edges, r[0], r[1])
    removeLoops(edges)

#redirects all adges from b to a
def merge(edges, a, b):
    #just make a copy of input for iteration
    for f,s in list(edges):
        if f==b:
            edges.remove((f,s))
            edges.append((a,s))
        if s==b:
            edges.remove((f,s))
            edges.append((f,a))

def removeLoops(edges):
	for f,s in list(edges):
		if f==s:
			edges.remove((f,s))

def vertexes(edges):
	v = set()
	for f,s in edges:
		v.add(f)
		v.add(s)
	return len(v)

def readEdges():
    edges = []
    with open(FILE, 'r') as f:
        for l in f.readlines():
            nodeLine = l.split()
            fst = nodeLine[0]
            for snd in nodeLine[1:]:
                if (snd, fst) not in edges:
                    edges.append((fst, snd))
    return edges

if __name__ == '__main__':
    e = readEdges()
    print(f"len e = {len(e)}  e = {e}")
    r = []
    for i in range(0,ROUNDS):
        print(f"i = {i}")
        r.append(minCut(list(e)))
    print(f"results = {r}")
    print("Min: " + str(min(r)))
