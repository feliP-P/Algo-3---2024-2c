import heapq
from collections import deque
aristas = [[] for _ in range(10000)]
distances1 = {node: float('inf') for node in range(10000)}
distances2 = {node: float('inf') for node in range(10000)}
 
def dijkstra(start, target, distances):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances[start] = 0
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == target:
            return distances
        for neighbor, weight in aristas[current_node]:
            distance = current_distance + weight
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
 
def main():
    n,m = map(int, input().split())
    for _ in range(m):
        u,v,w = map(int, input().split())
        aristas[u].append((v,2*w))
        aristas[v].append((u,2*w))
    mindist0 = dijkstra(0, n-1,distances1)
    mindistN = dijkstra(n-1, 0,distances2)
 
    costoTodosCaminosMin = 0
    for actual in range(n):
        for vecino, peso in aristas[actual]:
            if (peso + mindistN[vecino] + mindist0[actual]) == mindist0[n-1]:
                costoTodosCaminosMin += peso
    print(costoTodosCaminosMin)
 
if __name__ == "__main__":
    main()
