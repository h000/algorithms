#include <string>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    int visited[200];
    queue<int>  q;
    
    memset(visited, 0, sizeof(visited));
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            q.push(i);
        if (q.empty())
            continue;
        while (!q.empty()) {
            int tmp = q.front();
            q.pop();
            visited[tmp] = 1;
            for (int j = 0; j < n; ++j) {
                if (computers[tmp][j] == 1 && visited[j] == 0)
                    q.push(j);
            }
        }
        ++answer;
    }
    return answer;
}