class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) return s;
        int i,j,size, longest=0,left;
        for(i=0;i<s.size();i++) {
            size=-1;
            for(j=0;j+i<s.size()&&i-j>=0;j++) {
                if(s[i-j]==s[j+i]) size+=2;
                else break;
            }
            if(longest <= size) {
                left = i-j+1;
                longest = size;
            }
            size=0;
            for(j=0;j+i+1<s.size()&&i-j>=0;j++) {
                if(s[i-j]==s[j+i+1]) size+=2;
                else break;
            }
            if(longest < size) {
                left = i-j+1;
                longest = size;
            }
        }
        return s.substr(left,longest);
    }
};
