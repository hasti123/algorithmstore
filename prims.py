#PS5

#MST-PRIM
import sys

class Vertex:
    #list of edges?
    def __init__(self):
        self.index = 0
        self.key = sys.maxsize
        self.pi = 0

class Edge:
    def __init__(self):
        self.weight = 0
        self.u = Vertex()
        self.v = Vertex()

class Graph:
    def __init__(self):
        self.adj = []
        self.E = []
        self.V = []

def decreaseKey(r,w):
    r.key = w

def extractMin(pq):
    pq.sort(key = lambda x: x.key, reverse=True)
    return pq.pop()

def weight(G, u, v):
    for vertex in G.adj[u.index]:
        if vertex.index == v.index:
            for edge in G.E:
                if edge.u.index == u.index and edge.v.index == v.index:
                    return edge.weight
    return 0


def mstPrim(graph):
    pq = []
    mst = []
    edgePQ = []
    
    for v in graph.V:
        pq.append(v)

    decreaseKey(pq[0],0)
    
    while(pq):
        u = extractMin(pq)
        
        for v in graph.adj[u.index]:
            if any(x.index == v.index for x in pq) and weight(graph,u,v) < v.key:
                v.pi = u
                decreaseKey(v,weight(graph,u,v))

        mst.append(u)
        
    result = 0
    for v in mst:
        result = result + v.key

    print(result)
    
def isNumber(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

def runPrims():
    numArray = []
    
    f = open('mst.txt','r')
    c = f.read()
    f.close()
    charArray = c.split()
    for char in charArray:
        if isNumber(char):
            numArray.append(int(char))

    length = 0
    currentVertex = 0
    v = Vertex()

    g = Graph()

    for j in range(numArray[0]):
        v = Vertex()
        v.index = j
        g.V.append(v)

    adj = []
    
    for i in range(1, len(numArray)):
        if numArray[i] != 0:
            edge = Edge()
            edge.weight = numArray[i]
            edge.u = g.V[currentVertex]
            edge.v = g.V[length]
            g.E.append(edge)
            adj.append(g.V[length])

        if length == 8:
            g.adj.append(adj)
            adj = []
            length = -1
            currentVertex = currentVertex + 1

        length = length + 1

    mstPrim(g)
