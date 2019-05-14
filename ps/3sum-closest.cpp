class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int i, left, right, closest = 100000000;
        sort(nums.begin(), nums.end());
        for(i=0;i<nums.size()-1;i++) {
            int local_closest;
            left = i+1;
            right = nums.size()-1;
            while (left < right) {
                int cur = nums[i] + nums[left] + nums[right] - target;
                if (abs(cur) < abs(closest)) {
                    closest = cur;
                }
                if (cur < 0) left++;
                else if (cur > 0) right--;
                else return target;
            }
        }
        return closest+target;
    }
};
