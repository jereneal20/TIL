class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int i;
        long long int sum=0, max=0, normal_sum=0;
        for(i=0;i<A.size();i++){
            sum += A[i]*i;
            normal_sum += A[i];
        }
        max = sum;

        for(i=1;i<A.size();i++){
            // cout << sum - normal_sum + A[i-1]*((long)A.size()) << endl;
            if (max < sum - normal_sum + A[i-1]*((long)A.size())) {
                max = sum - normal_sum + A[i-1]*((long)A.size());
            }
            sum = sum - normal_sum + A[i-1]*((long)A.size());
        }
        return max;
    }
};
