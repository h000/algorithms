#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int count[50][3];

int main() {
    int R, N;
    string s;
    string friends[50];
    int score = 0;
    int max_score = 0;

    cin >> R >> s >> N;
    for (int i = 0; i < R; ++i)
        memset(count[i], 0, sizeof(count[i]));
    for (int i = 0; i < N; ++i) {
        cin >> friends[i];
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < R; ++j) {
            if (s[j] == friends[i][j])
                score += 1;
            else if ((s[j] == 'S' && friends[i][j] == 'P') ||
                (s[j] == 'P' && friends[i][j] == 'R') ||
                (s[j] == 'R' && friends[i][j] == 'S'))
                score += 2;
            
            if (friends[i][j] == 'S')
                ++count[j][0];
            else if (friends[i][j] == 'R')
                ++count[j][1];
            else
                ++count[j][2];
        }
    }

    for (int i = 0; i < R; ++i) {
        int tmp;
        tmp = max(count[i][1] + count[i][2] * 2, count[i][0] + count[i][1] * 2);
        tmp = max(tmp, count[i][0] * 2 + count[i][2]);
        max_score += tmp;
    }
    cout << score << endl;
    cout << max_score << endl;
    return 0;
}