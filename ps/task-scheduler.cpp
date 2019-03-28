class Solution {
public:
    int leastInterval(vector<char>& tasks, int n){
        int nums[26] = {0};
        int i, res=0;
        if (n==0) return tasks.size();
        for(i=0;i<tasks.size();i++){
            nums[tasks[i]-'A'] += 1;
        }
        sort(nums, nums+26, greater<int>());
        while (true) {
            for (i=0; nums[i] > 0 && i < n + 1;i++){
                nums[i]--;
                res++;
            }
            sort(nums, nums+26, greater<int>());
            if(nums[0]==0) break;
            res += (n + 1 - i);
            // cout << res << endl;
        }
        return res;
    }

};
