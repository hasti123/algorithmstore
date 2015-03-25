#Bellman-Ford algorithm
import sys

class Vertex:
    #list of edges?
    def __init__(self):
        self.index = 0
        self.d = sys.maxsize
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

def initSingleSource(G, sourceIndex):
    G.V[sourceIndex].d = 0

def relax(G, u, v):
    for vertex in G.adj[u.index]:
        if v.d > u.d + weight(G,u,v):
            v.d = u.d + weight(G,u,v)
            v.pi = u

def weight(G, u, v):
    for vertex in G.adj[u.index]:
        if vertex.index == v.index:
            for edge in G.E:
                if edge.u.index == u.index and edge.v.index == v.index:
                    return edge.weight

    return 0

def BellmanFord(G):
    initSingleSource(G, 0)

    for i in range(len(G.V)):
        for edge in G.E:
            relax(G,edge.u,edge.v)

    for edge in G.E:
        if edge.v.d > edge.u.d + weight(G,edge.u,edge.v):
            print("returned False, there is no shortest path.")
            return False

    counter = 0
    
    for v in G.V:
        print("[{0}]: {1}".format(counter, v.d))
        counter = counter + 1

    return True

def isNumber(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

def runBF():
    numArray = []
    
    f = open('sp.txt','r')
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

    BellmanFord(g)
