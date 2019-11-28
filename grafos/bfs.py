def bfs(G,s):
    branco = "branco"
    cinza = "cinza"
    preto = "preto"
    Q = []
    cor = []
    d = []
    pai = []
    for x in G:
        d.append(float('inf'))
        pai.append(None)
        cor.append(branco)
    d[s] = 0
    pai[s] = None
    cor[s] = cinza
    Q.append(s)
    ini = 0
    while ini!=len(Q):
        u = Q[ini]
        for v in G[u]:
            if cor[v] == branco:
                d[v] = d[u] + 1
                pai[v] = u
                cor[v] = cinza
                Q.append(v)
        cor[u] = preto
        ini += 1
    return d

def calcDist(s,v,G):
    d = bfs(G,s)
    return d[v]

def diametro(s,T):
    d = bfs(T,s)
    a = d.index(max(d))
    d = bfs(T, a)
    b = d.index(max(d))
    return d[b]


grafo = [[1,4],[0,5],[6],[7],[0],[1,6],[2,5,7],[3,6]]

#               0---1   2   3
#               |   |   |   |
#               4   5---6---7
#
#Teste calcDiametro
assert diametro(1,grafo)==6
assert diametro(0,grafo)==6

#Teste calcDist
assert calcDist(0,1,grafo) == 1
assert calcDist(1,3,grafo) == 4
assert calcDist(2,3,grafo) == 3
assert calcDist(3,4,grafo) == 6
assert calcDist(4,2,grafo) == 5
assert calcDist(5,6,grafo) == 1
assert calcDist(7,5,grafo) == 2


grafoB = [[1,4],[0,2,5],[1],[4],[0,3],[1]]
#       0---1---2
#         \   \
#       3---4   5
#
#Teste calcDiametro
assert diametro(1,grafoB) == 4
assert diametro(0,grafoB) == 4

#Teste calcDist
assert calcDist(0,1,grafoB) == 1
assert calcDist(1,3,grafoB) == 3
assert calcDist(2,3,grafoB) == 4
assert calcDist(3,4,grafoB) == 1
assert calcDist(4,5,grafoB) == 3


grafoC = [[1,3],[0,2,4],[1,5],[0],[4],[5]]
#   0---1---2
#   |   |   |
#   3   4   5
#
#Teste calcDiametro
assert diametro(1,grafoC) == 4
assert diametro(2,grafoC) == 4

#Teste calcDist
assert calcDist(0,1,grafoC) == 1
assert calcDist(1,5,grafoC) == 2
assert calcDist(2,3,grafoC) == 3
assert calcDist(3,5,grafoC) == 4