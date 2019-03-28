class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i;
        unordered_map<int, int> map;
        for (i=0; i<nums.size();i++){
            map[nums[i]] = i;
        }
        for (i=0; i<nums.size();i++){
            if (map.find(target-nums[i]) != map.end() && map[target-nums[i]] != i){
                vector<int> res;
                res.push_back(map[target-nums[i]]);
                res.push_back(i);
                return res;
            }
        }
        vector<int> res;
        return res;
    }
};
