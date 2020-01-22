from random import randrange

class Vertice:
    def __init__(self, num):
        self.num = num
        self.pai = None
        self.pertenceQ = True
        self.visitado = False
        self.adj = []

    def __str__(self):
        return "Vertice(%d)" % (self.num)

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]
        self.numArestas = 0
    

    def addAresta(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])
        self.vertices[v].adj.append(self.vertices[u])
        
        self.numArestas += 1

# grafo = [[1,4],[0,5],[3,5,6],[2,6,7],[0],[1,2,6],[2,3,5,7],[3,6]]



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
        return False

    d = bfs(G,randrange(len(G.vertices)))

    return float('inf') not in d   

def randomTreeRandomWalk(n):
    G = Grafo(n)
    u = randrange(n)
    G.vertices[u].visitado = True

    while G.numArestas < (n-1):
        v = randrange(n)
        if not G.vertices[v].visitado:
           G.addAresta(u,v)
        G.vertices[v].visitado = True
        u = v
    
    return G

    
def diametro(T):
    s = randrange(len(T.vertices))
    d = bfs(T,s)
    a = d.index(max(d))
    d = bfs(T, a)
    b = d.index(max(d))
    return d[b]

def diametroMedio(n):
    somadiam = 0
    for x in range(0, 500):
        A = randomTreeRandomWalk(n)
        if ehArvore(A):
            diam = diametro(A)
            somadiam += diam
        else:
            print("ERRO")
    return somadiam/500
        

#Teste pro eh_arvore
def TesteRandom():
    g = Grafo(9)

    g.addAresta(0,1)
    g.addAresta(0,2)
    g.addAresta(1,2)
    g.addAresta(1,5)
    g.addAresta(2,3)
    g.addAresta(2,4)
    g.addAresta(3,4)
    g.addAresta(3,5)
    g.addAresta(4,7)
    g.addAresta(5,6)
    g.addAresta(5,7)
    g.addAresta(6,8)
    g.addAresta(6,7)
    g.addAresta(7,8)

    #teste pro ehArvore
    assert ehArvore(g) == False

    #teste pro diametro
    assert diametro(g) == 4

if __name__ == "__main__":
    TesteRandom()
    print(250, diametroMedio(250))
    print(500,diametroMedio(500))
    print(750,diametroMedio(750))
    print(1000,diametroMedio(1000))
    print(1250,diametroMedio(1250))
    print(1500,diametroMedio(1500))
    print(1750,diametroMedio(1750))
    print(2000,diametroMedio(2000))

