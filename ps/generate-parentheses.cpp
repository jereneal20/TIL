class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        recurse(res, n, 0, "");
        return res;
    }
    void recurse(vector<string> &res, int n, int open, string str) {
        if (str.size() == 2*n) {
            if (open == 0) res.push_back(str);
            return;
        }
        if (open <= n) recurse(res, n, open + 1, str + "(");
        if (open >= 1) recurse(res, n, open - 1, str + ")");
    }
};
