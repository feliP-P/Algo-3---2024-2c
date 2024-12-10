import heapq
from collections import deque

aristas = [[] for _ in range(10000)]
distances = {node: float('inf') for node in range(10000)}
predecessors = [[] for node in range(10000)]


def dijkstra(start, target):
    """
    Encuentra el camino mínimo entre dos nodos en un grafo usando el algoritmo de Dijkstra.

    :param graph: Diccionario de adyacencia donde las claves son nodos y los valores son
                  listas de tuplas (vecino, peso).
    :param start: Nodo de inicio.
    :param target: Nodo objetivo.
    :return: Una tupla (distancia, camino) donde distancia es la longitud del camino mínimo
             y camino es una lista con los nodos en el camino.
    """
    # Cola de prioridad para almacenar los nodos y su distancia
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    # Diccionarios para almacenar la distancia mínima y los predecesores
    
    distances[start] = 0
    

    while priority_queue:
        # Extraer el nodo con la menor distancia
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si llegamos al nodo objetivo, construimos el camino
        if current_node == target:
            caminomin = [(current_node,0,0)]
            siguiente = deque([current_node])
            while siguiente:
                current_node = siguiente.popleft()
                for predecessor in predecessors[current_node]:
                    siguiente.append(predecessor[0])
                    caminomin.append(predecessor)
                
            return current_distance, caminomin

        # Explorar los vecinos del nodo actual
        for neighbor, weight in aristas[current_node]:
            distance = current_distance + weight

            # Si encontramos una distancia menor, actualizamos
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                predecessors[neighbor] = [(current_node,neighbor,weight)]
                heapq.heappush(priority_queue, (distance, neighbor))
            # si encontramos otro camino posible
            elif distances[neighbor] == distance:
                predecessors[neighbor].append((current_node,neighbor,weight))

    # Si no se encuentra un camino al nodo objetivo
    return float('inf'), []

def agregarArista(u,v,w):
    aristas[u].append((v,w))
    aristas[v].append((u,w))

def main():
    n,m = map(int, input().split())
    for _ in range(m):
        u,v,w = map(int, input().split())
        agregarArista(u,v,2*w)
    distance, path = dijkstra(0, n-1)
    print(path)
    costoTodosCaminosMin = 0
    for arista in path:
        costoTodosCaminosMin += arista[2]
    print(costoTodosCaminosMin)

if __name__ == "__main__":
    main()
