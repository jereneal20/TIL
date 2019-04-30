class Solution {
public:
    string reverseVowels(string s) {
        vector<char> tmp;
        int i;
        for(i=0;i<s.size();i++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
                tmp.push_back(s[i]);
        }
        for(i=0;i<s.size();i++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
                s[i] = tmp.back();
                tmp.pop_back();
            }
            
        }
        return s;
    }
};
