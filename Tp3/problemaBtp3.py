grafo = [[0 for j in range(203)] for i in range(203)]
grafo2 = [[0 for j in range(203)] for i in range(203)]
def agregar_arista(origen, destino, peso):
    grafo[origen][destino] = peso
 
def bfs(inicio, final, parent,n):
    visitados = {inicio}
    cola = [inicio]
        
    while cola:
        nodo_actual = cola.pop(0)
        
        for vecino, capacidad in zip(range(203),grafo[nodo_actual]):
                if capacidad > 0 and vecino not in visitados:
                    visitados.add(vecino)
                    parent[vecino] = nodo_actual
                    if vecino == final:
                        return True
                    cola.append(vecino)
    return False
    
def edmonds_karp( inicio, final,n):
    max_flow = 0
    parent = {}
    while bfs(inicio, final, parent,n):
        path_flow = float('Inf')
        s = final
        while s != inicio:
            path_flow = min(path_flow, grafo[parent[s]][s])
            s = parent[s]
                
        max_flow += path_flow
        v = final
                
        while v != inicio:
            u = parent[v]
            grafo[u][v] -= path_flow
            grafo[v][u] += path_flow
            grafo2[u][v] += path_flow
            grafo2[v][u] -= path_flow
            v = u
 
    return max_flow
 
def main():
    n,m = map(int, input().split())
    valoresEntrada = list(map(int, input().split()))
    valoresMaximos = list(map(int, input().split()))
    flowentrada = 0
    flowsalida = 0
    for i in range(n):
        flowentrada += valoresEntrada[i]
        flowsalida += valoresMaximos[i]
        agregar_arista(0, i+1, valoresEntrada[i])
        agregar_arista(i+101, 202, valoresMaximos[i])
        agregar_arista(i+1, i+101, valoresMaximos[i])
    for i in range(m):
        u,v = map(int, input().split())
        agregar_arista(u, v+100, 100)
        agregar_arista(v, u+100, 100)
 
    maxflow = edmonds_karp(0, 202, n+1)
 
    if flowentrada != flowsalida or maxflow != flowentrada:
        print("NO")
    else:
        print("YES")
        
        for i in range(1, n+1):
            print(*grafo2[i][101:n+101])
        #for i in range(1,n+1):
        #    for j in range(101, 101 +n):
        #        print(grafo[j][i], end=" ")
        #    print()
if  __name__ == "__main__":
    main()