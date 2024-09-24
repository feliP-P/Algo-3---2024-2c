import math
import numpy as np

def borg(lista, i, b,w):
    if i >= len(lista)-2:
        return 0
    elif lista[i] >= lista[w] and lista[i] <= lista[b]:
        minim = (borg(lista, i+1, b, w) +1)
    elif lista[i] > lista[b] and lista[i] >= lista[w]:
        minim = min(borg(lista, i+1, i, w), borg(lista, i+1, b, w) + 1)
    elif lista[i] < lista[w] and lista[i] <= lista[b]:
        minim = min(borg(lista, i+1, b, i), borg(lista, i+1, b, w) + 1)
    elif lista[i] < lista[w] and lista[i] > lista[b]:
        minim = min( borg(lista, i+1, i, w), borg(lista, i+1, b, i), borg(lista, i+1, b, w) + 1 )
    return minim

def borgdinamico(lista, i, b,w):
    if i >= len(lista)-2:
        return 0 
    if memoria[i][b][w] != -1:
        return memoria[i][b][w]
    elif lista[i] >= lista[w] and lista[i] <= lista[b]:
        minim = (borg(lista, i+1, b, w) +1)
    elif lista[i] > lista[b] and lista[i] >= lista[w]:
        minim = min(borg(lista, i+1, i, w), borg(lista, i+1, b, w) + 1)
    elif lista[i] < lista[w] and lista[i] <= lista[b]:
        minim = min(borg(lista, i+1, b, i), borg(lista, i+1, b, w) + 1)
    elif lista[i] < lista[w] and lista[i] > lista[b]:
        minim = min( borg(lista, i+1, i, w), borg(lista, i+1, b, i), borg(lista, i+1, b, w) + 1 )
    memoria[i][b][w] = minim  # guardamos el resultado en memoria para evitar volver a calcularlo
    return minim


n = int(input())
while n != -1:
    lista = list(map(int, input().split()))
    lista.append(0)
    lista.append(math.inf)
    #print(borg(lista, 0, n, n+1))

    memoria = [[[-1 for i in range(n+2)] for j in range(n+2)] for k in range(n+2)]
        
    print(borgdinamico(lista, 0, n, n+1))

    n = int(input())

#algunos casos de test que usé:
#n = 30
#128 93 113 133 37 168 176 32 57 181 49 143 43 106 56 60 91 15 161 56 25 42 63 129 39 32 1 187 57 178
#14

#7 8 9 1 2 3 6 5 4 9 8 7

#n = 30
#69 84 164 36 4 7 172 189 14 135 3 54 25 69 145 79 166 176 30 104 91 45 183 109 29 98 137 120 80 18
#rta = 14

#traduje a c++ en chat gpt y devolvió el siguiente código (funcionó):
""" 
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

vector<vector<vector<int>>> memoria;

int borg(const vector<int>& lista, int i, int b, int w) {
    if (i >= lista.size() - 2) {
        return 0;
    } else if (lista[i] >= lista[w] && lista[i] <= lista[b]) {
        return borg(lista, i + 1, b, w) + 1;
    } else if (lista[i] > lista[b] && lista[i] >= lista[w]) {
        return min(borg(lista, i + 1, i, w), borg(lista, i + 1, b, w) + 1);
    } else if (lista[i] < lista[w] && lista[i] <= lista[b]) {
        return min(borg(lista, i + 1, b, i), borg(lista, i + 1, b, w) + 1);
    } else if (lista[i] < lista[w] && lista[i] > lista[b]) {
        return min({borg(lista, i + 1, i, w), borg(lista, i + 1, b, i), borg(lista, i + 1, b, w) + 1});
    }
    return 0; // Por si acaso, aunque no debería llegar aquí.
}

int borgdinamico(const vector<int>& lista, int i, int b, int w) {
    if (i >= lista.size() - 2) {
        return 0;
    }
    if (memoria[i][b][w] != -1) {
        return memoria[i][b][w];
    } else if (lista[i] >= lista[w] && lista[i] <= lista[b]) {
        memoria[i][b][w] = borgdinamico(lista, i + 1, b, w) + 1;
    } else if (lista[i] > lista[b] && lista[i] >= lista[w]) {
        memoria[i][b][w] = min(borgdinamico(lista, i + 1, i, w), borgdinamico(lista, i + 1, b, w) + 1);
    } else if (lista[i] < lista[w] && lista[i] <= lista[b]) {
        memoria[i][b][w] = min(borgdinamico(lista, i + 1, b, i), borgdinamico(lista, i + 1, b, w) + 1);
    } else if (lista[i] < lista[w] && lista[i] > lista[b]) {
        memoria[i][b][w] = min({borgdinamico(lista, i + 1, i, w), borgdinamico(lista, i + 1, b, i), borgdinamico(lista, i + 1, b, w) + 1});
    }
    return memoria[i][b][w];
}

int main() {
    int n;
    cin >> n;
    while (n != -1) {
        vector<int> lista(n + 2);
        for (int i = 0; i < n; ++i) {
            cin >> lista[i];
        }
        lista[n] = 0;
        lista[n + 1] = numeric_limits<int>::max();

        memoria.assign(n + 2, vector<vector<int>>(n + 2, vector<int>(n + 2, -1)));
        
        cout << borgdinamico(lista, 0, n, n + 1) << endl;

        cin >> n;
    }
    return 0;
}
"""