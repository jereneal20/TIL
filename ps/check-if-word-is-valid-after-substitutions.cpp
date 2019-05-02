class Solution {
public:
    bool isValid(string S) {
        vector<char> stk;
        int i;
        for(i=0;i<S.size();i++) {
            if (stk.empty() || S[i] != 'c') {
                stk.push_back(S[i]);
                continue;
            }
            if (stk.back() != 'b') return false;
            stk.pop_back();
            if (stk.empty() || stk.back() != 'a') return false;
            stk.pop_back();
        }
        if (!stk.empty()) return false;
        return true;
    }
};
