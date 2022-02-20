class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stk = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) =='(') {
                stk.push(i);
            } else {
                if (stk.size() == 0) {
                    stk.push(i);
                }else if (s.charAt(stk.peek()) == '(') {
                    stk.pop();
                } else {
                    stk.push(i);
                }
            }
        }
        int max_interval = 0;
        int prev_idx = -1;
        if (stk.size() == 0) {
            return s.length();
        }
        stk.push(s.length());
        for(int i = 0; i< stk.size();i++) {
            max_interval = Math.max(max_interval, stk.get(i) - prev_idx - 1);
            prev_idx = stk.get(i);
        }
        System.out.println(stk);

        return max_interval;
    }
}