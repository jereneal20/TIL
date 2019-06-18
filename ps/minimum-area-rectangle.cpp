struct hash_pair{
    size_t operator()(const pair<int, int> &pair) const{
        return hash<int>()(pair.first) ^ hash<int>()(pair.second);
    }
};
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        unordered_map<pair<int, int>, int,hash_pair> map;
        for(auto point: points) {
            map[pair(point[0],point[1])] = 1;
        }
        int i,j;
        int res = 100000000;
        for(i=0;i<points.size();i++) {
            for(j=i+1;j<points.size();j++) {
                if (points[i][0] == points[j][0] || 
                   points[i][1] == points[j][1])
                    continue;
                if (map.find(pair(points[i][0],points[j][1])) == map.end() ||
                   map.find(pair(points[j][0],points[i][1])) == map.end()) 
                    continue;
                res = min(res, abs(points[j][0]-points[i][0])*abs(points[i][1]-points[j][1]));
                
            }
        }
        if (res == 100000000) return 0;
        return res;
    }
};
