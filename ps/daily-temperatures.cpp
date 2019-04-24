class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(),0);
        vector<int> stk;
        int i;
        for(i=0;i<T.size();i++){
            while (!stk.empty() && T[stk.back()]<T[i]) {
                res[stk.back()] = i-stk.back();
                stk.pop_back();
            } 
            stk.push_back(i);
        }
        return res;
    }
};
