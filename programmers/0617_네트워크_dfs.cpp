#include <string>
#include <vector>
#include <cstring>

using namespace std;

int visited[200];

void dfs(int i, int n, vector<vector<int>> computers) {
    visited[i] = 1;
    for (int j = 0; j < n; ++j) {
        if (computers[i][j] == 1 && !visited[j])
            dfs(j, n, computers);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    memset(visited, 0, sizeof(visited));
    
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i, n, computers);
            ++answer;
        }
    }
    return answer;
}