class Solution {
public:
    int isValidChar(char chr) {
        if(chr == '+' || chr == '-' || ('0' <= chr && chr <= '9')) {
            return true;
        }
        return false;
    }
    int myAtoi(string str) {
        int i;
        long res = 0;
        bool isPositive = true;
        for(i=0;i<str.size();i++) {
            if(str[i] != ' ') break;
        }
        if (!isValidChar(str[i])) return 0;
        if(str[i] == '-') { isPositive = false; i++; }
        else if(str[i] == '+') { i++; }
        
        for(;i<str.size();i++) {
            if(!isValidChar(str[i]) || str[i] =='+' || str[i] == '-') break;
            if(isPositive) res = res*10 + (str[i] - '0');
            else res = res*10 - (str[i] - '0');
            if (res > INT_MAX) return INT_MAX;
            if (res < INT_MIN) return INT_MIN;
        }
        return res;
    }
};
