class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res(nums.size(), -1);
        vector<int> stk;
        int i;
        for(i=0;i<nums.size()*2;i++) {
            if (stk.empty()) stk.push_back(i%nums.size());
            else {
                while (!stk.empty() && nums[stk.back()] < nums[i%nums.size()]) {
                    res[stk.back()] = nums[i%nums.size()];
                    stk.pop_back();
                }
                stk.push_back(i%nums.size());
            }
        }
        return res;
    }
};
