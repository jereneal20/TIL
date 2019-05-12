class Solution {
public:
    int maxArea(vector<int>& height) {
        int i, left=0,right=1;
        for(i=2;i<height.size();i++){
            int curMax =(right-left)*max(height[left],height[right]);
            if (right == i-1 && curMax < (i-left)*max(height[left],height[i])){
                right=i;
            }
            if ()
                
        }
    }
};
