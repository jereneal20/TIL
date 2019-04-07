class Solution {
public:
    vector<int> diStringMatch(string S) {
        int low = 0, high = S.size(), i;
        vector<int> res;        
        for(i=0;i<S.size();i++) {
            if (S[i] == 'I') res.push_back(low++);
            else res.push_back(high--);
        }
        res.push_back(low);
        return res;
    }
};
