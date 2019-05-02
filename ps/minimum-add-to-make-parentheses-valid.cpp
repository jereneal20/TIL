class Solution {
public:
    int minAddToMakeValid(string S) {
        int i, res=0, size=0;
        for(i=0;i<S.size();i++) {
            if (size==0 && S[i] == ')') res++;
            else if (S[i] == ')') size--;
            else size++;
        }
        return size+res;
    }
};
