class Solution {
public:
    int maximumSwap(int num) {
        int i,res, maxNum=-1, maxIdx, leftIdx = -1, rightIdx;
        string str = to_string(num);
        // 뒤에서 오면서 이때까지 중 가장 큰 값을 찾는다. 그 뒤 그것보다 작은게 오면 그 둘은 스왑 대상.
        // 최대한 앞쪽에서 바꾸는게 좋으므로 앞으로 가면서 해당 조건이 만족하면 계속 leftIdx를 업데이트
        // max가 나왔지만 그 이후로 그것보다 작은 값이 안나왔으면 그 앞쪽은 바꿀게 없는것이므로 안바꾼다.
        
        for(i=str.size()-1;i>=0;i--){
            if (maxNum < str[i]) {
                maxNum = str[i];
                maxIdx = i;
            }
            
            if (maxNum > str[i]) {
                leftIdx = i;
                rightIdx = maxIdx;
            }
        }
        
        if (maxNum != -1 && leftIdx != -1) {
            swap(str[leftIdx], str[rightIdx]);
        }
        res = stoi(str);
        return res;
    }
};
