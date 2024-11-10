#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <climits>

using namespace std;

vector<int> clasificadas(100002, 0);
vector<int> low(100001, -1);
vector<int> disc(100001, -1);
vector<bool> visitado(100001, false);

class Grafo {
public:
    int V, tiempo;
    vector<vector<pair<int, int>>> grafo;

    Grafo(int vertices) : V(vertices), tiempo(0), grafo(vertices) {}

    void agregar_arista(int u, int v, int i) {
        grafo[u].emplace_back(v, i);
        grafo[v].emplace_back(u, i);
    }

    void dfs_puente(int u, int iid) {
        visitado[u] = true;
        disc[u] = low[u] = tiempo++;
        
        for (auto [v, i] : grafo[u]) {
            if (i == iid) continue;
            if (visitado[v]) {
                low[u] = min(low[u], disc[v]);
            } else {
                dfs_puente(v, i);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    clasificadas[i] = 2; // Marcar como puente
                }
            }
        }
    }
};

class UnionFind {
public:
    vector<int> parent;

    UnionFind(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_sets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    n += 1;

    vector<tuple<int, int, int, int>> aristas;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        aristas.emplace_back(u, v, w, i);
    }
    aristas.emplace_back(0, 0, INT_MAX, -1);
    sort(aristas.begin(), aristas.end(), [](auto& a, auto& b) {
        return get<2>(a) < get<2>(b);
    });

    UnionFind uf(n);
    Grafo grafo(n);
    int i = 0;

    while (i < m) {
        if (get<2>(aristas[i]) == get<2>(aristas[i + 1])) {
            int j = i;
            vector<tuple<int, int, int>> sinclasificar;
            while (j < m && get<2>(aristas[j]) == get<2>(aristas[i])) {
                auto [x, y, w, idd] = aristas[j];
                int fx = uf.find(x);
                int fy = uf.find(y);
                if (fx != fy) {
                    clasificadas[idd] = 1;  // Marcar como posible puente
                    grafo.agregar_arista(fx, fy, idd);
                    sinclasificar.emplace_back(fx, fy, idd);
                }
                ++j;
            }

            for (auto [a, _, _] : sinclasificar) {
                if (!visitado[a]) {
                    grafo.dfs_puente(a, -1);
                }
            }

            for (auto [x, y, idd] : sinclasificar) {
                grafo.grafo[x].clear();
                grafo.grafo[y].clear();
                visitado[x] = visitado[y] = false;
                uf.union_sets(x, y);
            }
            i = j;
            grafo.tiempo = 0;
        } else {
            auto [u, v, _, idd] = aristas[i];
            int fu = uf.find(u);
            int fv = uf.find(v);
            if (fu != fv) {
                uf.union_sets(fu, fv);
                clasificadas[idd] = 2;  // No es puente
            }
            ++i;
        }
    }

    for (int resultado = 0; resultado < m; ++resultado) {
        if (clasificadas[resultado] == 2) {
            cout << "any" << endl;
        } else if (clasificadas[resultado] == 1) {
            cout << "at least one" << endl;
        } else {
            cout << "none" << endl;
        }
    }

    return 0;
}
