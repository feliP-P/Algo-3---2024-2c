clasificadas = [0] * 100002
low = [-1] * 100001
disc = [-1] * 100001
visitado = [False] * 100001
 
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[] for _ in range(vertices)]
        self.tiempo = 0
 
 
    def agregar_arista(self, u, v,i):
        self.grafo[u].append((v,i))
        self.grafo[v].append((u,i))
 
    def dfs_puente(self, u,iid):
        visitado[u] = True
        disc[u] = low[u] = self.tiempo
        self.tiempo += 1
 
        for v,i in self.grafo[u]:
            if i == iid: 
                continue
            if visitado[v]:
                low[u] = min(low[u], disc[v])
            else:
                self.dfs_puente(v,i)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    clasificadas[i] = 2
 
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
 
def main():
    try:
        n, m = map(int, input().split())
        n+=1
        aristas = [list(map(int, input().split())) + [i] for i in range(m)]
        aristas.append((0,0,float('inf')))
        aristas.sort(key=lambda x: x[2])

        uf = UnionFind(n) 
        grafo = Grafo(n)
    #separamos las aristas con mismo peso de las demás
        i = 0
        while i < m:
            if aristas[i][2] == aristas[i + 1][2]:
                j = i
                sinclasificar = []
                while j < m and aristas[j][2] == aristas[i][2]:
                    x, y, w, idd = aristas[j]
                    fx = uf.find(x)
                    fy = uf.find(y)
                    if fx != fy:
                        clasificadas[idd] = 1
                        grafo.agregar_arista(fx, fy, idd)
                        sinclasificar.append((fx,fy,idd))
 
                    j += 1

                for a,_,_ in sinclasificar:
                    if not visitado[a]:
                        grafo.dfs_puente(a,-1)
 
                for x,y,idd in sinclasificar:
                    grafo.grafo[x].clear()
                    grafo.grafo[y].clear()
                    visitado[x] = visitado[y] = False
                    uf.union(x, y)
                i = j
                grafo.tiempo = 0
 
            else:
                u, v, _, idd = aristas[i]
                fu = uf.find(u)
                fv = uf.find(v)
                if fu != fv:
                    uf.union(fu, fv)
                    clasificadas[idd] = 2
                i += 1
 
        for resultado in range(m):
            if clasificadas[resultado] == 2:
                print("any")
            elif clasificadas[resultado] == 1:
                print("at least one")
            else:
                print("none")
    except EOFError:
        pass
 
if __name__ == "__main__":
    main()
"""
7 9
1 2 1
1 3 2
2 3 2
2 4 3
3 4 4
3 5 5
4 5 1
4 6 6
5 7 7


"""
"""
any
at least one
at least one
any
none
none
any
any
any
"""