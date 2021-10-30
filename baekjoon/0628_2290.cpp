#include <iostream>
#include <vector>

using namespace std;

int s;
string  n;
string  display[23];

vector<int> number[10] = {
    // 그려지는 부분을 7개 부분으로 나누고 각 숫자에 그려져야하는 부분
    {1, 2, 3, 5, 6, 7},
    {3, 6},
    {1, 3, 4, 5, 7},
    {1, 3, 4, 6, 7},
    {2, 3, 4, 6},
    {1, 2, 4, 6, 7},
    {1, 2, 4, 5, 6, 7},
    {1, 3, 6},
    {1, 2, 3, 4, 5, 6, 7},
    {1, 2, 3, 4, 6, 7}
};

void print_line(int x, int y, int vh) {
    if (vh == 0) {
        for (int i = 1; i < s + 1; ++i) {
            display[y][x + i] = '-';
        }
    }
    if (vh == 1) {
        for (int i = 1; i < s + 1; ++i) {
            display[y + i][x] = '|';
        }
    }
}

void print(int idx, int start) {

    for (int i = 0; i < number[idx].size(); ++i) {
        if (number[idx][i] == 1)
            print_line(start, 0, 0);
        else if (number[idx][i] == 2)
            print_line(start, 0, 1);
        else if (number[idx][i] == 3)
            print_line(start + s + 1, 0, 1);
        else if (number[idx][i] == 4)
            print_line(start, s + 1, 0);
        else if (number[idx][i] == 5)
            print_line(start, s + 1, 1);
        else if (number[idx][i] == 6)
            print_line(start + s + 1, s + 1, 1);
        else if (number[idx][i] == 7)
            print_line(start, 2 * s + 2, 0);
    }
}

int main() {
    cin >> s >> n;
    int dis_y = 2 * s + 3;
    for (int i = 0; i < dis_y; ++i) {
        display[i] = string(n.size() * (s + 3), ' ');
    }
    for (int i = 0; i < n.size(); ++i) {
        print(n[i] - '0', i * (s + 2 + 1));
    }
    for (int i = 0; i < dis_y; ++i)
        cout << display[i] << endl;
}