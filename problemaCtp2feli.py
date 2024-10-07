import math
from collections import deque
    
def main():
    n = int(input())
    atajos = list(map(int,input().split()))
    if n > 1:
        caminominimo = [math.inf for _ in range(n)]
        visitados = set([0,1])
        cola = deque([1])
        caminominimo[0] = 0
        caminominimo[atajos[0]-1] = min(1,caminominimo[atajos[0]-1])
        caminominimo[1] = 1
        if atajos[0]-1 not in visitados:
            visitados.add(atajos[0]-1)
            cola.append(atajos[0]-1)
        while cola:
            node = cola.popleft()
            caminominimo[atajos[node]-1] = min(caminominimo[node] + 1, caminominimo[atajos[node]-1])
            caminominimo[node-1] = min(caminominimo[node-1],caminominimo[node] +1)
            if node != n-1:
                caminominimo[node+1] = min(caminominimo[node+1],caminominimo[node] +1)
            if (atajos[node]-1) not in visitados:
                visitados.add(atajos[node]-1)
                cola.append(atajos[node]-1)
            if node<n-1 and node+1 not in visitados:
                visitados.add(node+1)
                cola.append(node+1)
            if node-1 not in visitados:
                visitados.add(node-1)
                cola.append(node-1)
        for i in range(len(caminominimo)):
            print(caminominimo[i] ,end=" ")
    else:
        print(0)

if __name__ == '__main__':
    main()