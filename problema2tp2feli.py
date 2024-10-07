from collections import deque
 
def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    
    # Leer el grafo
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
 
    # Inicializar colores y contadores
    color = [-1] * n
    color[0] = 0
    contador = [1, 0]  # contador[0] para el color 0, contador[1] para el color 1
    visitados = set([0])
    cola = deque([0])  # Usar una cola para BFS
 
    # BFS
    while cola:
        node = cola.pop()
        for v in graph[node]:
            if v not in visitados:
                color[v] = 1 - color[node]
                contador[color[v]] += 1
                visitados.add(v)
                cola.append(v)
 
    # Calcular el número máximo de aristas
    max_aristas = contador[0] * contador[1]
    
    # Comprobar la condición final
    resultado = max(0, max_aristas - n + 1)
    print(resultado)
 
if __name__ == '__main__':
    main()
'''
7
1 2
2 3
4 1
1 5
5 6
7 6
'''