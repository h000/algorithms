#include <string>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    int dist[20001];
    
    memset(dist, 0, sizeof(dist));
    queue<int>  q;
    
    q.push(1);
    while (!q.empty()) {
        int n = q.front();
        q.pop();
        for (int i = 0; i < edge.size(); ++i) {
            if (n == edge[i][0]) {
                int tmp = 1 + dist[n];
                if ((edge[i][1] != 1 && dist[edge[i][1]] == 0) || dist[edge[i][1]] > tmp) {
                    dist[edge[i][1]] = tmp;
                    q.push(edge[i][1]);
                }
            }
            else if (n == edge[i][1]) {
                int tmp = 1 + dist[n];
                if ((edge[i][0] != 1 && dist[edge[i][0]] == 0) || dist[edge[i][0]] > tmp) {
                    dist[edge[i][0]] = tmp;
                    q.push(edge[i][0]);
                }
            }
        }
    }
    int max = 0;
    for (int i = 0; i <= n; ++i) {
        if (max < dist[i]) {
            answer = 1;
            max = dist[i];
        }
        else if (max == dist[i])
            ++answer;
    }
    return answer;
}