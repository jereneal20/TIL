class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> res;
        vector<int> max_res;
        int i,j;
        
        for (i=0;i<=k;i++){
            if (nums1.size() < i || nums2.size() < k-i) continue;
            res = maxNumber(maxNumber(nums1,i),maxNumber(nums2,k-i));
            for(int i=0; i<res.size(); ++i)
                cout << res[i] << ' ';
            cout << endl;
            if (max_res.empty()) {
                max_res = res;
            } else {
                for (j=0;j< max_res.size();j++) {
                    if (max_res[j] > res[j]) {
                        break;
                    } else if (max_res[j] < res[j]){
                        max_res = res;
                        break;
                    }
                }
            }
        }
        return max_res;
    }
    
    vector<int> maxNumber(vector<int> nums1, int k) {
        vector<int> res;
        int i;
        if (k==0) return res;
        for(i=0;i<nums1.size();i++) {
            if (res.empty() || k-res.size() == nums1.size()-i) {
                res.push_back(nums1[i]);
            } else {
                if (res.back() < nums1[i]) {
                    res.pop_back();
                    i--;
                } else {
                    if (res.size() < k)
                        res.push_back(nums1[i]);
                }
            }
        }
        return res;
    }

    vector<int> maxNumber(vector<int> nums1, vector<int> nums2) {
        vector<int> res;
        int i=0,j=0;
        while (i<nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                res.push_back(nums2[j++]);
            } else if (nums1[i] > nums2[j]){
                res.push_back(nums1[i++]);
            } else {
                int k=0;
                while (i+k < nums1.size() && j+k < nums2.size()) {
                    if (nums1[i+k] == nums2[j+k]) k++;
                    else break;
                }
                if (i+k == nums1.size()) res.push_back(nums2[j++]);
                else if (j+k == nums2.size()) res.push_back(nums1[i++]);
                else if (nums1[i+k] < nums2[j+k]) res.push_back(nums2[j++]);
                else res.push_back(nums1[i++]);
            }
        }
        while (i<nums1.size()){
            res.push_back(nums1[i++]);
        }
        while (j<nums2.size()){
            res.push_back(nums2[j++]);
        }
        return res;
    }
};
