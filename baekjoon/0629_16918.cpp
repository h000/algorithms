#include <iostream>
#include <vector>

using namespace std;

char board[200][200];
int time[200][200];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    int R, C, N;
    cin >> R >> C >> N;

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 'O')
                time[i][j] = 3;
            else
                time[i][j] = 0;
        }
    }

    for (int t = 1; t <= N; ++t) {
        if (t % 2 == 0) {
            for (int i = 0; i < R; ++i) {
                for (int j = 0; j < C; ++j) {
                    if (board[i][j] == '.') {
                        board[i][j] = 'O';
                        time[i][j] = t + 3;
                    }
                }
            }
            continue;
        }
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (time[i][j] == t) {
                    board[i][j] = '.';
                    time[i][j] += 3;
                    for (int k = 0; k < 4; ++k) {
                        if (i + dx[k] >= 0 && i + dx[k] < R && j + dy[k] >= 0 && j + dy[k] < C) {
                            board[i + dx[k]][j + dy[k]] = '.';
                            time[i][j] = t + 3;
                        }
                    }
                }
            }
        }
        
    }
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            cout << board[i][j];
        }
        cout << endl;
    }
    return 0;
}