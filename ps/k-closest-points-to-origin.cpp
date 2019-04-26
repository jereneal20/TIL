class Comparison {
public:
    bool operator() (vector<int> a, vector<int> b) {
        return a[0]*a[0]+a[1]*a[1]<b[0]*b[0]+b[1]*b[1];
    }
};

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        priority_queue<vector<int>, vector<vector<int>>, Comparison> pq;
        vector<vector<int>> res;
        int i;
        if (points.size() <= K) return points;
        for(i=0;i<points.size();i++) {
            pq.push(points[i]);
            if (pq.size() > K) pq.pop();
        }
        for(i=0;i<K;i++) {
            res.push_back(pq.top());
            pq.pop();
        }
        return res;
    }
};
