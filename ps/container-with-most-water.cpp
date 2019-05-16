class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0,right=height.size()-1, vol=-1;
        while (left < right) {
            vol = max(vol, min(height[left],height[right])*(right-left));
            if (height[left] < height[right]) left++;
            else right--;
        }
        return vol;
    }
};
