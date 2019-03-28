class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i,j, start = 0, longest = 0;
        unordered_map<char, int> map;
        
        for (i=0;i<s.size();i++){
            if (map.find(s[i]) != map.end() ) {
                j = start;
                start = map[s[i]] + 1;
                while (j < start) {
                    // Delete until new start pos
                    map.erase(s[j]);
                    j++;
                }
            }
            longest = max(longest, i-start+1);
            map[s[i]] = i;
        }
        return longest;
    }
};
