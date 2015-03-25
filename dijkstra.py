import sys

class Vertex:
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

def length(G, u, v):
    for vertex in G.adj[u.index]:
        if vertex.index == v.index:
            for edge in G.E:
                if edge.u.index == u.index and edge.v.index == v.index:
                    return edge.weight
    return sys.maxsize

def extractMin(pq, dist):
    minimum = sys.maxsize
    index = 0
    count = 0
    
    for v in pq:
        if dist[v.index] < minimum:
            minimum = dist[v.index]
            index = count
            
        count = count + 1
          
    return index

def Dijkstra(G, source):
    dist = []
    previous = []
    pq = []
    
    for i in range(len(G.V)):
        dist.append(sys.maxsize)
        previous.append(-1)
        
    dist[source] = 0

    for v in G.V:
        pq.append(v)

    while pq:
        u = pq.pop(extractMin(pq,dist))
        for neighbor in G.adj[u.index]:
            alt = dist[u.index] + length(G, u, neighbor)
            if alt < dist[neighbor.index]:
                dist[neighbor.index] = alt
                previous[neighbor.index] = u.index


    result = 0

    for i in range(len(dist)):
        print("[{0}]: {1}".format(i, dist[i]))

def isNumber(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

def runSP():
    numArray = []
    
    f = open('SPinput.txt','r')
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
        
    startVertex = numArray[1];
    adj = []
    
    for i in range(2, len(numArray)):
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

    Dijkstra(g, startVertex)
