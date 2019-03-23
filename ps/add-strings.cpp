class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() -1, j = num2.size()-1, added;
        bool carry = false;
        string res = "";
        while (true) {
            if (i < 0 && j < 0) break;
            if (j < 0) {
                added = num1[i] - '0';
            } else if (i < 0) {
                added = num2[j] - '0';
            } else {
                added = num1[i] - '0' + num2[j] - '0';
            }
            if (carry) added += 1;
            
            if (added >= 10) {
                res += added - 10 + '0';
                carry = true;
            } else {
                res += added + '0';
                carry = false;
            }
            i--;
            j--;
        }
        if (carry) res += "1";
        string rev = "";
        for (i=res.size()-1;i>=0;i--) rev += res[i];
        return rev;
    }
};
