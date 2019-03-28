class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int i,j;
        if (strs.size() == 0) return "";
        for (j=0;j<strs[0].size();j++){
            char tmp = strs[0][j];
            for (i=0;i<strs.size();i++) {
                if (strs[i][j] != tmp) return strs[0].substr(0,j);
            }
        }
        return strs[0];
    }
};
