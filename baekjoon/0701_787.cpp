class Solution {
public:
    struct node {
        int src;
        int cost;
        int k;
    };
    
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        queue<struct node>  q;
        struct node    nd;
        nd.src = src;
        nd.cost = 0;
        nd.k = 0;
        int min = -1;
        
        q.push(nd);
        while (!q.empty()) {
            struct node tmp = q.front();
            q.pop();
            for (int i = 0; i < flights.size(); ++i) {
                if (tmp.k > k + 1)
                    break;
                if ((min == -1 || min > tmp.cost)) {
                    if (tmp.src == dst)
                        min = tmp.cost;
                    else if (tmp.src == flights[i][0]) {
                        struct node tmp2 = q.front();
                        tmp2.src = flights[i][1];
                        tmp2.cost = tmp.cost + flights[i][2];
                        tmp2.k = tmp.k + 1;
                        q.push(tmp2);
                    }
                }
            }
            if (tmp.k > k + 1)
                break;
        }
        return min;
    }
};