import random
import heapq
from random import randrange

class Vertice:
    def __init__(self, num):
        self.num = num
        self.pai = None
        self.pertenceQ = True
        self.chave = float("inf")
        self.adj = []

    def __str__(self):
        return "Vertice(%d)" % (self.num,)

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]
        self.numAresta = 0
        self.peso = [ [float("inf") for i in range(n)] for i in range(n)]
        self.arestas = []

    def addAresta(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])
        self.vertices[v].adj.append(self.vertices[u])
        self.numAresta+=1

    def addPeso(self, u, v, peso):
        self.peso[u][v] = peso
        self.peso[v][u] = peso

def bfs(G,s):
    branco="branco"
    cinza="cinza"
    preto ="preto"
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
    while Q!=[]:
        i = Q.pop(0)
        u = G.vertices[i]
        for v in u.adj:
            if cor[v.num] == branco:

                d[v.num]=d[u.num]+1
                pai[v.num] = u.num
                cor[v.num] = cinza
                Q.append(v.num)
        cor[u.num] = preto
    return d

def fazArvore(v):
    A = Grafo(len(v))
    for x in v:
        if x.pai!=None:
            A.addAresta(x.num,x.pai.num)
            A.addPeso(x.num,x.pai.num, x.chave)
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

def eh_arvore(G):
    if G.numAresta!= len(G.vertices)-1:
        print(G.numAresta)
        print(len(G.vertices))
        return False
        
    d = bfs(G,randrange(len(G.vertices)))
  
    for x in d:
    
        if x == float('inf'):
            return False
        
    return True

def adicionarAresta(A):
    for x in A.vertices:
        for y in A.vertices:
            if x!=y:
                A.addAresta(x.num,y.num)
    return A

def randomTreePrim(n):
    G = adicionarAresta(Grafo(n))
    s = randrange(n)
    G = MstPrim(G,s)
    return G
def TesteMST_Kruskal():
    g = Grafo(9)

    g.addAresta(0,1)
    g.addPeso(0,1,4)

    g.addAresta(0,2)
    g.addPeso(0,2,8)

    g.addAresta(1,2)
    g.addPeso(1,2,11)

    g.addAresta(1,5)
    g.addPeso(1,5,8)

    g.addAresta(2,3)
    g.addPeso(2,3,7)

    g.addAresta(2,4)
    g.addPeso(2,4,1)

    g.addAresta(3,4)
    g.addPeso(3,4,6)

    g.addAresta(3,5)
    g.addPeso(3,5,2)

    g.addAresta(4,7)
    g.addPeso(4,7,2)

    g.addAresta(5,7)
    g.addPeso(5,7,4)

    g.addAresta(5,6)
    g.addPeso(5,6,7)
    
    g.addAresta(6,8)
    g.addPeso(6,8,9)

    g.addAresta(6,7)
    g.addPeso(6,7,14)

    g.addAresta(7,8)
    g.addPeso(7,8,10)
    
  
    
    A = MstPrim(g,0)
    
    # for x in A.vertices:
       
    #     for y in x.adj:
    #         print("(%s %s) -> peso = %f" %(str(x), str(y), A.peso[x.num][y.num]))
    
    pesoMin = 0
    for x in A.peso:
        for y in x:
            if y != float("inf"):
                pesoMin+=y
    assert pesoMin/2 == 37

    
if __name__ == "__main__":
    TesteMST_Kruskal()
    
    # randomTreeKruskal(4)
    

#  python -m cProfile -s time .\kruskal.py