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
        aristas.append([u - 1, v - 1, w, False,i])
    
    #sort
    aristas.sort(key=lambda x: x[2])
    # Search for equal weights and separate them in different groups
    aristasrepe = [[] for i in range(m)]
    aristassinrepe = [] 
    i = 0
    while i < m:
        if i == m-1:
            aristassinrepe.append(aristas[i])
            i += 1

        elif aristas[i][2] == aristas[i+1][2]:
            aristas[i][3] = True
            aristassinrepe.append(aristas[i])
            aristasrepe[aristas[i][4]] = [aristas[i],aristas[i+1]]
            j = i + 2
            while j<m and aristas[j][2] == aristas[i][2]:
                aristasrepe[aristas[i][4]].append(aristas[j])
                j += 1
            i = j
        else:
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
    def puentes(aristass):
        graph = Grafo(n)
        for u,v in aristass:
            graph.agregar_arista(u, v)
        return graph.encontrar_puentes()


    #agregamos 0,1,2 al final para representar si estan en todos alguno o ningun arbol
    for u, v, w, b, i in aristassinrepe:
        #print(parent)
        #si es un peso unico
        if b == False:
            if find(u)!= find(v):
                union(u, v)
                mst.append((u, v))
                clasificadas.append((u,v,w,i,0))
                #mstg.append(find(v))
            else:
                clasificadas.append((u,v,w,i,2))
        #si es un peso repetido
        else:
            #nodosmin = mstg.copy()
            #aristasmstg = []
            aristasconrepe = mst.copy()
            sinclasificar = []
            for x,y,weigt,bolean,j in aristasrepe[i]:
                #si es una arista que une dos componentes distintas
                if find(x)!= find(y):
                    #aristasmstg.append((find(x),find(y)))
                    aristasconrepe.append((x,y))
                    sinclasificar.append((x,y,j))
                #si es una arista de una misma componente conexa
                else:
                    clasificadas.append((x,y,w,j,2))
            setpuentes = puentes(aristasconrepe)
            for x,y,j in sinclasificar:
                union(x,y)
                mst.append((x,y))
                if (x,y) in setpuentes or (y,x) in setpuentes:
                    clasificadas.append((x,y,w,j,0))
                else:
                    clasificadas.append((x,y,w,j,1))

    clasificadas.sort(key=lambda x: x[3])
    for i in range(len(clasificadas)):
        if clasificadas[i][4] == 0:
            print('any')
        elif clasificadas[i][4] == 1:
            print('at least one')
        elif clasificadas[i][4] == 2:
            print('none')
        else:
            print('error')
    

if __name__ == '__main__':
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