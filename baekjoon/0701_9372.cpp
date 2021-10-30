#include <iostream>
#include <vector>
#include <cstring>

using namespace std;


int main() {
    int T, N, M;
    

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> M;
        for (int m = 0; m < M; ++m) {
            int a, b;
            cin >> a >> b;
        }
        cout << N - 1 << endl;
    }
    return 0;
}