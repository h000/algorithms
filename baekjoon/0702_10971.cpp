#include <iostream>
#include <vector>

using namespace std;

int ans = 987654321;
int N;
int W[10][10];

void find_path(int start, int last, int visited, int dist) {
    if (visited == (1 << N) - 1) {
        if (W[last][start] != 0)
            ans = min(ans, dist + W[last][start]);
        return ;
    }
    for (int i = 0; i < N; ++i) {
        if (((visited & (1 << i)) == 0) && (W[last][i] != 0))
            find_path(start, i, visited | (1 << i), dist + W[last][i]);
    }
}

int main() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j)
            cin >> W[i][j];
    }

    for (int i = 0; i < N; ++i)
        find_path(i, i, 1 << i, 0);
    cout << ans << endl;
}