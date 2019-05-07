class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i,j,k;
        
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (i=0;i<nums.size();i++) {
            if (i != 0 && nums[i] == nums[i-1]) continue;
            j = i+1;
            k = nums.size()-1;
            while(j < k) {
                if (nums[j] + nums[k] + nums[i] > 0) {
                    k--;
                } else if (nums[j] + nums[k] + nums[i] < 0) {
                    j++;
                } else {
                    vector<int> tmp;
                    tmp.push_back(nums[i]);
                    tmp.push_back(nums[j]);
                    tmp.push_back(nums[k]);
                    res.push_back(tmp);
                    while (true) {
                        if (j < k && nums[j+1] == nums[j]) j++;
                        else if (j < k && nums[k-1] == nums[k]) k--;
                        else {
                            j++;
                            k--;
                            break;
                        }
                    }
                }
            }
        }
        return res;
    }
};
/*
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i,j;
        unordered_map<int, int> map;
        vector<vector<int>> res;
        // sort(nums.begin(), nums.end());
        for (i=0;i<nums.size();i++) {
            // find -nums[i] == a + b
            map[-nums[i]] = i;
        }
        for (i=0;i<nums.size();i++) {
            for (j=i+1;j<nums.size();j++) {
                if (map.count(nums[i] + nums[j]) > 0 && 
                   map[nums[i] + nums[j]] != i && map[nums[i] + nums[j]] != j) {
                    vector<int> tmp;
                    tmp.push_back(- (nums[i] + nums[j]));
                    tmp.push_back(nums[i]);
                    tmp.push_back(nums[j]);
                    map.erase(nums[i] + nums[j]);
                    res.push_back(tmp);
                }
            }
        }
        return res;
    }
};
*/
