class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i;
        bool canFlowered;
        for(i=0;i<flowerbed.size();i++) {
            canFlowered = flowerbed[i] ? false : true;
            if (i != 0) canFlowered &= flowerbed[i-1] ? false : true;
            if (i != flowerbed.size()-1) canFlowered &= flowerbed[i+1] ? false : true;
            
            if (canFlowered) {
                flowerbed[i] = 1;
                n--;
            }
        }
        return n<=0?true:false;
    }
};
