#include <string>
#include <vector>
#include <cstring>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    int res[101][101];
    
    for (int i = 0; i < n; ++i)
        memset(res, 0, sizeof(res));
    
    for (int i = 0; i < results.size(); ++i) {
        res[results[i][0]][results[i][1]] = 1;
        res[results[i][1]][results[i][0]] = -1;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (res[i][j] == 1) {
                for (int k = 1; k <= n; ++k) {
                    if (res[j][k] == 1) {
                        res[i][k] = 1;
                        res[k][i] = -1;
                    }
                }
            }
            else if (res[i][j] == -1) {
                for (int k = 1; k <= n; ++k) {
                    if (res[j][k] == -1) {
                        res[i][k] = -1;
                        res[k][i] = 1;
                    }
                }
            }
        }
    }
    
    for (int i = 1; i <= n; ++i) {
        int count = 0;
        for (int j = 1; j <= n; ++j) {
            if (res[i][j] != 0)
                ++count;
        }
        if (count == n - 1)
            ++answer;
    }
    
    return answer;
}