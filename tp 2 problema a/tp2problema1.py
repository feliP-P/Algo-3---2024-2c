from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.grafo = defaultdict(list)  # Diccionario de listas de adyacencia
        self.tiempo = 0  # Tiempo para rastrear orden de visita

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def dfs_puente(self, u, visitado, padres, low, disc, puentes):
        # Marcar el nodo actual como visitado
        visitado[u] = True

        # Inicializar los tiempos de descubrimiento y low-link
        disc[u] = low[u] = self.tiempo
        self.tiempo += 1

        # Iterar por los vecinos del nodo actual
        for v in self.grafo[u]:
            if not visitado[v]:  # Si el vecino no ha sido visitado
                padres[v] = u
                self.dfs_puente(v, visitado, padres, low, disc, puentes)

                # Actualizar el valor low del nodo u
                low[u] = min(low[u], low[v])

                # Verificar si la arista (u, v) es un puente
                if low[v] > disc[u]:
                    puentes.append((u, v))
            elif v != padres[u]:  # Si el vecino ha sido visitado y no es el padre
                low[u] = min(low[u], disc[v])

    def encontrar_puentes(self):
        # Inicializar estructuras auxiliares
        visitado = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        padres = [-1] * self.V
        puentes = []

        # Llamar a DFS para cada nodo no visitado
        for i in range(self.V):
            if not visitado[i]:
                self.dfs_puente(i, visitado, padres, low, disc, puentes)

        return puentes


def main():
    n,m = map(int, input().split())
    aristas = []
    for i in range(m):
        u, v, w = map(int, input().split())
        aristas.append((u - 1, v - 1, w, False))
    
    #sort
    aristas.sort(key=lambda x: x[2])
    # Search for equal weights and separate them in different groups
    aristasrepe = {}
    aristassinrepe = [] 
    i = 0
    while i < m-1:
        if aristas[i][2] == aristas[i+1][2]:
            aristas[i][3] = True
            aristassinrepe.append(aristas[i])
            aristasrepe[aristas[i][2]] = [aristas[i][2],aristas[i+1][2]]
            j = i + 2
            while aristas[j][2] == aristas[i][2]:
                aristasrepe[aristas[i][2]].append(aristas[j][2])
                j += 1
            i = j
        else:
            aristasrepe[aristas[i][2]] = [aristas[i][2]]
            aristassinrepe.append(aristas[i])
    
        i += 1
    # Kruskal's algorithm
    clasificadas = []
    mst = []
    parent = list(range(n))

    def find(x):
        if parent[x]!= x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)

    #ejecutamos dfs y buscamos los puentes del grafo
    def puentes(aristas):
        graph = Grafo(5)
        #graph = [[] for _ in range(n)]
        for u,v in aristas:
            graph.agregar_arista(u, v)
            #graph[u].append(v)
            #graph[v].append(u)
        #visitados = set([aristas[0][0]])
        visitados = [False for _ in range(n)]
        visitados[aristas[0][0]] = True
        cola = deque([aristas[0][0]])
        bridges = set()
        while cola:
            node = cola.popleft()
            for child in graph[node]:
                if child not visitados:
                    visitados[child] = True
                    cola.append(child)
                    bridges.add((min(node, child), max(node, child)))
        return bridges


    #agregamos 0,1,2 al final para representar si estan en todos alguno o ningun arbol
    for u, v, w, b in aristas:
        #si es un peso unico
        if b == True:
            if find(u)!= find(v):
                union(u, v)
                mst.append((u, v, w))
                clasificadas.append((u,v,w,0))
            else:
                clasificadas.append((u,v,w,2))
        #si es un peso repetido
        else:
            aristasconrepe = mst
            sinclasificar = []
            for x,y in aristasrepe[u,v,w,b]:
                #si es una arista de una misma componente conexa
                if find(x)== find(y):
                    clasificadas.append((x,y,w,2))
                #si es una arista que une dos componentes distintas
                else:
                    aristasconrepe.append(u,v,w)
                    sinclasificar.append(u,v)
            setpuentes = puentes(aristasconrepe)
            for x,y in sinclasificar:
                if x,y,w in setpuentes:
                    clasificadas.append(x,y,w,0)
                else:
                    clasificadas.append((x,y,w,1))

        
    
    # Calculate the total weight of the MST
    print(mst)
    total_weight = sum(w for u, v, w in mst)
    print(total_weight)

if __name__ == '__main__':
    main()

