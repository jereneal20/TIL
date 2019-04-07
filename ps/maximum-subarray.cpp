class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSoFar, rightMostMax, i;
        maxSoFar = nums[0];
        rightMostMax = nums[0];
        for ( i = 1;i<nums.size();i++) {
            rightMostMax = max(rightMostMax+nums[i], nums[i]);
            maxSoFar = max(maxSoFar, rightMostMax);
        }
        return maxSoFar;
    }
};

class Solution2 {
public:
    int maxSubArray(vector<int>& nums) {
        int maxVal, left, right, sum;
        recursion(nums, 0, nums.size()-1, sum, maxVal, left, right);
        return maxVal;
    }
    void recursion(vector<int>& nums, int l, int r, int &sum, int &maxVal, int &leftMostMax, int &rightMostMax) {
        int left_max, right_max, innerRightMast, innerLeftMast;
        int lsum, rsum;
        if (l == r) {
            maxVal = nums[l];
            leftMostMax = nums[l];
            rightMostMax = nums[l];
            sum = nums[l];
            return;
        }
        
        recursion(nums, l, (l+r)/2, lsum, left_max, leftMostMax, innerRightMast);
        recursion(nums, (l+r)/2+1, r, rsum, right_max, innerLeftMast, rightMostMax);
        
        maxVal = max(max(left_max, right_max), innerRightMast+innerLeftMast);
        rightMostMax = max(rightMostMax, rsum+innerRightMast);
        leftMostMax = max(leftMostMax, lsum+innerLeftMast);
        sum = lsum+rsum;
    }
}
