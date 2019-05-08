class Solution {
public:
    string decodeString(string s) {
        int i, count, idx;
        vector<int> stk;
        
        for(i=0;i<s.size();i++) {
            if ('0' <= s[i] && s[i] <= '9'){
                stk.push_back(i);
                while (s[i] != '[') {
                    i++;
                }
            } else if (s[i] == ']') {
                idx = stk.back();
                stk.pop_back();
                i = decode(s, idx, i);
            }
        }
        return s;
    }
    
    int decode(string& s, int start, int end) {
        int idx = start, i, count=0;
        string res= "";
        string res2= "";
        while (s[idx] != '[') {
            count += s[idx]-'0';
            idx++;
            count *= 10;
        }
        count /= 10;
        
        for(i=idx+1;i<end;i++) {
            res += s[i];
        }
        for(i=0;i<count;i++){
            res2 += res;
        }
        
        s.replace(start, end - start + 1, res2);
        return start + res2.size() - 1;
    }
    
};
