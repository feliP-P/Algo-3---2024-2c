
def dantzing(grafo):
    n = len(grafo)
    for k in range(n):
        for i in range(k):
            grafo[i][k] = min(grafo[i][j] + grafo[j][k] for j in range(k))
            grafo[k][i] = min(grafo[k][j] + grafo[j][i] for j in range(k))

def floydwarshall(grafo):
    n = len(grafo)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])

def main():
    n = int(input())
    grafoprov = []
    grafo = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        adyacencias = list(map(int,input().split()))
        grafoprov.append(adyacencias)
    ordenCronologico = list(map(int, input().split()))
    inv = list(reversed(ordenCronologico))
    for i in range(n):
        for k in range(n):
            grafo[i][k] = grafoprov[inv[i]-1][inv[k]-1]
#    for i in range(n):
#        k = ordenCronologico[n-1-i] - 1
#        print(k)
#        for j in range(n):
#            grafo[j][i] = grafoprov[j][k]

    for i in range(n):
        print(grafo[i])
    dantzing(grafo)
    dantzing(grafoprov)
    for i in range(n):
        print(grafoprov[i])
    for i in range(n):
        print(grafo[i])

if __name__ == "__main__":
    main()

"""
3
0 1 4
1 0 1
1 3 0
1 2 3
"""