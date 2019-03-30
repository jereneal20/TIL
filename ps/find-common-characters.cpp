class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        unordered_map<char, int> map;
        int i=0, j;
        for (i=0;i<A.size();i++) {
            unordered_map<char, int> map2;
            for (j=0;j<A[i].size();j++) {
                map2[A[i][j]] += 1;
                if (i==0) map[A[i][j]] += 1;
            }
            for (auto it = map.begin(); it != map.end(); it++) {
                map[it->first] = min(map2[it->first], it->second);
            }
        }
        
        vector<string> res;
        for (auto it = map.begin(); it != map.end(); it++) {
            for (i=0;i<it->second;i++){
                string s;
                s += it->first;
                res.push_back(s);
            }
        }
        return res;
    }
};
