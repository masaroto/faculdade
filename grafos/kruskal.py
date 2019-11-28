import random
from random import randrange
import timeit

class Vertice:
    def __init__(self, num):
        self.num = num
        self.pai = None
        self.rank = None
        self.adj = []

    def __str__(self):
        return "Vertice(%d)" % (self.num)

class Aresta:
    def __init__(self,v1,v2,peso):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]
        self.numArestas = 0
        self.arestas = []

    def addAresta(self, u, v, peso):
        self.vertices[u].adj.append(self.vertices[v])
        self.vertices[v].adj.append(self.vertices[u])
        v1 = self.vertices[u]
        v2 = self.vertices[v]
        self.arestas.append(Aresta(v1,v2,peso))
        self.numArestas+=1


        
        


def bfs(G,s):
    branco = "branco"
    cinza = "cinza"
    preto = "preto"
    Q = []
    cor = []
    d = []
    pai = []
    for x in G.vertices:
        d.append(float('inf'))
        pai.append(None)
        cor.append(branco)
    d[s] = 0
    pai[s] = None
    cor[s] = cinza
    Q.append(s)
    ini = 0
    while ini!=len(Q):
        i = Q[ini]
        u = G.vertices[i]
        for v in u.adj:
            if cor[v.num] == branco:
                d[v.num] = d[u.num]+1
                pai[v.num] = u.num
                cor[v.num] = cinza
                Q.append(v.num)
        cor[u.num] = preto
        ini += 1
    return d 

def ehArvore(G):
    if G.numArestas!= len(G.vertices)-1:
        print(G.numAresta)
        print(len(G.vertices)-1)
        return False

    d = bfs(G,randrange(len(G.vertices)))

    return float('inf') not in d
     

def MakeSet(x):
    x.pai = x
    x.rank = 0

def link(x,y):
    if x.rank > y.rank:
        y.pai = x
    else:
        x.pai = y
        if x.rank == y.rank:
            y.rank += 1 

def FindSet(x):
    if x != x.pai:
        x.pai = FindSet(x.pai)
        return x.pai
    return x.pai

def union(x,y):
    link(FindSet(x), FindSet(y))


def MST_Kruskal(G):
    A = Grafo(len(G.vertices))
    for v in G.vertices:
        MakeSet(v)

    G.arestas.sort(key=lambda x: x.peso)

    for x in G.arestas:
        u = x.v1
        v = x.v2
        peso = x.peso
            
        if FindSet(u) != FindSet(v):
            A.addAresta(u.num,v.num,peso)    
            union(u,v)
    
    return A

def criaGrafoCompleto(A):
    for x in range (0, len(A.vertices)):
        for y in range (x+1, len(A.vertices)):
            peso = random.uniform(0,1)
            A.addAresta(x,y,peso)

    return A

def randomTreeKruskal(n):
    G = criaGrafoCompleto(Grafo(n))
    A = MST_Kruskal(G)

    return A
    
def diametro(T):
    s = randrange(len(T.vertices))
    d = bfs(T,s)
    a = d.index(max(d))
    d = bfs(T, a)
    b = d.index(max(d))
    
    return d[b]

def diametroMedio(n):
    """Stupid test function"""
    somadiam = 0
    for x in range(0, 500):
        A = randomTreeKruskal(n)
        if ehArvore(A):
            diam = diametro(A)
            somadiam += diam
        else:
            print("ERRO")

    return somadiam/500

def TesteMST_Kruskal():
    g = Grafo(9)

    g.addAresta(0,1,4)
    g.addAresta(0,2,8)
    g.addAresta(1,2,11)
    g.addAresta(1,5,8)
    g.addAresta(2,3,7)
    g.addAresta(2,4,1)
    g.addAresta(3,4,6)
    g.addAresta(3,5,2)
    g.addAresta(4,7,2)
    g.addAresta(5,6,7)
    g.addAresta(5,7,4)
    g.addAresta(6,8,9)
    g.addAresta(6,7,14)
    g.addAresta(7,8,10)
    
  
    A = MST_Kruskal(g)
    # for x in A.vertices:
    #     for y in x.adj:
    #         print("(%s %s) -> peso = %i" %(str(x), str(y), 0))

    pesoMin = 0
    for x in A.arestas:
        pesoMin+=x.peso
    pesoMin/2

    #Teste automatizados dos adjacentes de cada vertice
    assert (A.vertices[0].adj[0]) == A.vertices[1] 
    assert (A.vertices[0].adj[1]) == A.vertices[2]
    
    assert (A.vertices[1].adj[0]) == A.vertices[0]

    assert (A.vertices[2].adj[0]) == A.vertices[4] 
    assert (A.vertices[2].adj[1]) == A.vertices[0]

    assert (A.vertices[3].adj[0]) == A.vertices[5]

    assert (A.vertices[4].adj[0]) == A.vertices[2] 
    assert (A.vertices[4].adj[1]) == A.vertices[7]

    assert (A.vertices[5].adj[0]) == A.vertices[3] 
    assert (A.vertices[5].adj[1]) == A.vertices[7]
    assert (A.vertices[5].adj[2]) == A.vertices[6]

    assert (A.vertices[6].adj[0]) == A.vertices[5] 
    assert (A.vertices[6].adj[1]) == A.vertices[8]

    assert (A.vertices[7].adj[0]) == A.vertices[4] 
    assert (A.vertices[7].adj[1]) == A.vertices[5]

    assert (A.vertices[8].adj[0]) == A.vertices[6] 

    assert pesoMin == 37


def testeRandomKruskal(n):
    print(n, diametroMedio(n))

if __name__ == "__main__":
    TesteMST_Kruskal()
    # randomTreeKruskal(4)
    # testeRandomKruskal(250)
    print(timeit.timeit("diametroMedio(250)", setup="from __main__ import diametroMedio", number=1))

#  python -m cProfile -s time .\kruskal.py