def possible(distances,c,d):
    distance = 0
    i=0
    while i < len(distances) and c>0:
        distance += distances[i]
        if distance >= d:
            c-=1
            distance = 0
        i+=1
    t = False
    if c ==0:
        t = True
    return t

def binary_search(stalls, distances,c):
    maxdistance = (stalls[-1]-stalls[0])//(c-1)
    s = 1
    e = maxdistance
    continuation = True
    d = maxdistance//2
    while continuation:
        if possible(distances,c-1,d):
            s = d
            d += max(1,(e-d)//2)
        else:
            e = d-1
            d = d//2

        if s == e:
            continuation = False
    return e

def main():
    t = int(input())
    for i in range(t):
        n, c = map(int, input().split())
        stalls=[]
        for j in range(n):
            stalls.append(int(input()))
        stalls.sort()
        distances = [0 for _ in range(n)]
        for j in range(n-1):
            distances[j] = stalls[j+1] - stalls[j]
        print(binary_search(stalls,distances,c))


if __name__ == "__main__":
    main()


""" 
lo traduje a c++ con chat gpt y me quedó el siguiete código que pasó los tests:

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool possible(const vector<int>& distances, int c, int d) {
    int distance = 0;
    int i = 0;
    while (i < distances.size() && c > 0) {
        distance += distances[i];
        if (distance >= d) {
            c--;
            distance = 0;
        }
        i++;
    }
    return c == 0;
}

int binary_search(const vector<int>& stalls, const vector<int>& distances, int c) {
    int maxdistance = (stalls.back() - stalls.front()) / (c - 1);
    int s = 1;
    int e = maxdistance;
    bool continuation = true;
    int d = maxdistance / 2;

    while (continuation) {
        if (possible(distances, c - 1, d)) {
            s = d;
            d += max(1, (e - d) / 2);
        } else {
            e = d - 1;
            d = d / 2;
        }

        if (s == e) {
            continuation = false;
        }
    }
    return e;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, c;
        cin >> n >> c;
        vector<int> stalls(n);
        for (int j = 0; j < n; j++) {
            cin >> stalls[j];
        }
        sort(stalls.begin(), stalls.end());

        vector<int> distances(n - 1);
        for (int j = 0; j < n - 1; j++) {
            distances[j] = stalls[j + 1] - stalls[j];
        }

        cout << binary_search(stalls, distances, c) << endl;
    }

    return 0;
}

"""