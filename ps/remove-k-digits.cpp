class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> res;
        int i;
        k = num.size()-k;
        if (k == 0) return "0";
        for(i=0;i<num.size();i++) {
            if (res.empty()||k-res.size()==num.size()-i) res.push_back(num[i]);
            else {
                if (res.back() > num[i]) {
                    res.pop_back();
                    i--;
                } else {
                    if (res.size() < k)
                        res.push_back(num[i]);
                }
            }
        }
        string res_str = "";
        for (i=0;i<res.size();i++) {
            if (res_str.empty()&&res[i]=='0') continue;
            res_str += res[i];
        }
        if (res_str.size() == 0) res_str += '0';
        return res_str;
    }
};
