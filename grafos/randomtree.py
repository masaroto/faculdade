from random import randrange


grafo = [[1,4],[0,5],[3,5,6],[2,6,7],[0],[1,2,6],[2,3,5,7],[3,6]]
listCor = []
def numAresta(G):
    count = 0
    for x in G:
        count = count + len(x)
    return count/2

def bfs(G,s):
    Q = []
    cor = []
    d = []
    pai = []
    for x in range (0,len(G)):
        d.append(99999999)
        pai.append(None)
        cor.append("branco")
    d[s] = 0
    pai[s] = None
    cor[s] = "cinza"
    Q.append(s)
    while Q!=[]:
        u = Q.pop(0)

        for v in G[u]:
            if cor[v] == "branco":
                d[v]=d[u]+1
                pai[v] = u
                cor[v] = "cinza"
                Q.append(v)
        cor[u] = "preto"
    return d   
    
def calcDist(s,v):
    d = bfs(grafo,s)
    return d[v]

def calculaMax(d):
    x=0
    for i in range(0,len(d)):
        if x<d[i]:
            x=d[i]
            maiorV = i
    return maiorV

def diametro(T,s):
    d = bfs(T,s)
    a = calculaMax(d)
    d = bfs(T, a)
    b = calculaMax(d)
    return d[b]

def ehArvore(G,s):
    if numAresta(G) != len(G)-1:
        return False
    d = bfs(G,s)

    for x in d:
        if x == 99999999:
            return False
        
    return True

def random_tree_random_walk(n):
    G = []
    visitado = []
    for x in range (0,n):
        G.append([])
        visitado.append(False)
    
    u = randrange(n)
    visitado[u] = True

    while numAresta(G) < n-1:
        v = randrange(n)
        if not visitado[v]:
            G[u].append(v)
            G[v].append(u)
            visitado[v] = True
        u = v

    return G

    
def diametroMedio(n):
    somaDiam=0
    for x in range(0,500):
        a=random_tree_random_walk(n)
        if eh_arvore(a,randrange(n)):
            diam = diametro(a,randrange(n))
            somaDiam = somaDiam + diam
        
    return somaDiam/500
        
        
# print(random_tree_random_walk(5))

# Testes pro BFS
assert calcDist(1,0) == 1
assert calcDist(1,3) == 3
assert calcDist(1,7) == 3
assert calcDist(1,6) == 2

# Teste pro Diametro
assert diametro(grafo,0) == 5
assert diametro(grafo,1) == 5
assert diametro(grafo,2) == 5
assert diametro(grafo,3) == 5
assert diametro(grafo,4) == 5
assert diametro(grafo,5) == 5
assert diametro(grafo,6) == 5
assert diametro(grafo,7) == 5


#Teste pro eh_arvore

assert eh_arvore(grafo,0) == False

#teste pro diametroMedio
print(diametroMedio(250))

