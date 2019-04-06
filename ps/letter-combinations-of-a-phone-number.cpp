class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> letters;
        
        letters['2'] = "abc";
        letters['3'] = "def";
        letters['4'] = "ghi";
        letters['5'] = "jkl";
        letters['6'] = "mno";
        letters['7'] = "pqrs";
        letters['8'] = "tuv";
        letters['9'] = "wxyz";
        
        vector<string> res;
        if (digits.size() == 0) return res;
        enumerator(res, letters, digits, 0, "");
        return res;
    }
    
    void enumerator(vector<string> &res, unordered_map<char, string> letters, string digits, int idx, string alphs) {
        int i;
        if (digits.size() == idx) {
            res.push_back(alphs);
            return;
        }
        for (i = 0 ; i<letters[digits[idx]].size();i++) {
            enumerator(res, letters, digits, idx + 1, alphs + letters[digits[idx]][i]);
        }
        return;
    }
};
