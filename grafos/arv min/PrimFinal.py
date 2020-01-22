import random
import heapq
from random import randrange
import timeit


class Vertice:
    def __init__(self, num):
        self.num = num
        self.pai = None
        self.pertenceQ = True
        self.chave = float("inf")
        self.adj = []

    def __str__(self):
        return "Vertice(%d)" % (self.num)

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]
        self.numArestas = 0
        self.peso = [ [float("inf") for i in range(n)] for i in range(n) ]

    def addAresta(self, u, v, peso):
        self.vertices[u].adj.append(self.vertices[v])
        self.vertices[v].adj.append(self.vertices[u])
        self.peso[u][v] = peso
        self.peso[v][u] = peso
        self.numArestas += 1


        

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

def fazArvore(v):
    A = Grafo(len(v))
    for x in v:
        if x.pai!=None:
            A.addAresta(x.num,x.pai.num, x.chave)
            
    return A

def MstPrim(G, r):
    prim = []
    
    G.vertices[r].chave = 0
    Q = G.vertices.copy()
    while Q!=[]:
        u = min(Q, key=lambda x: x.chave)

        Q.remove(u)

        prim.append(u)
        for v in u.adj:
            if v.pertenceQ and G.peso[u.num][v.num] < v.chave:
                v.pai=u
                v.chave = G.peso[u.num][v.num]
        u.pertenceQ = False
        
    return fazArvore(prim)

def criaGrafoCompleto(A):
    for x in range (0, len(A.vertices)):
        for y in range (x+1, len(A.vertices)):
            peso = random.uniform(0,1)
            A.addAresta(x,y,peso)
                    
    return A

def randomTreePrim(n):
    G = criaGrafoCompleto(Grafo(n))
    s = randrange(n)
    G = MstPrim(G,s)
    return G

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
        A = randomTreePrim(n)
        if ehArvore(A):
            diam = diametro(A)
            somadiam += diam
        else:
            print("ERRO")
    print(somadiam/500)
    return somadiam/500


def TesteMST_Prim():
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

    A = MstPrim(g,0)
    pesoMin = 0

    for x in A.vertices:
        for y in x.adj:
            pesoMin +=  A.peso[x.num][y.num]
            # print("(%s %s) -> peso = %f" %(str(x), str(y), A.peso[x.num][y.num]))

    #Teste automatizados dos adjacentes de cada vertice
    assert (A.vertices[0].adj[0]) == A.vertices[1] 
    assert (A.vertices[0].adj[1]) == A.vertices[2]
    
    assert (A.vertices[1].adj[0]) == A.vertices[0]

    assert (A.vertices[2].adj[0]) == A.vertices[0] 
    assert (A.vertices[2].adj[1]) == A.vertices[4]

    assert (A.vertices[3].adj[0]) == A.vertices[5]

    assert (A.vertices[4].adj[0]) == A.vertices[2] 
    assert (A.vertices[4].adj[1]) == A.vertices[7]

    assert (A.vertices[5].adj[0]) == A.vertices[7] 
    assert (A.vertices[5].adj[1]) == A.vertices[3]
    assert (A.vertices[5].adj[2]) == A.vertices[6]

    assert (A.vertices[6].adj[0]) == A.vertices[5] 
    assert (A.vertices[6].adj[1]) == A.vertices[8]

    assert (A.vertices[7].adj[0]) == A.vertices[4] 
    assert (A.vertices[7].adj[1]) == A.vertices[5]

    assert (A.vertices[8].adj[0]) == A.vertices[6] 

    #Teste do peso minimo (Foi dividido por dois pois a soma do peso de u->v é feita, mas a v->u também é)
    assert pesoMin/2 == 37


    

    
    


    
if __name__ == "__main__":
    #TESTE MST_Prim
    TesteMST_Prim()

    #Teste DiametroMedio com Prim
    print(250, diametroMedio(250))
    print(500, diametroMedio(500))
    print(750, diametroMedio(750))
    # print(1000, diametroMedio(1000))
    # print(1250, diametroMedio(1250))
    # print(1500, diametroMedio(1500))
    # print(1750, diametroMedio(1750))
    # print(2000, diametroMedio(2000))
    
    

#  python -m cProfile -s time .\kruskal.py