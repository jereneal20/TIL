class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        m--;n--;
        while (0<=m && 0<=n) {
            if (nums1[m] <= nums2[n]) {
                nums1[m+n+1] = nums2[n];
                n--;
            } else {
                nums1[m+n+1] = nums1[m];
                m--;
            }
        }
        while (0<=n) {
            nums1[m+n+1] = nums2[n];
            n--;
        }
    }
};
