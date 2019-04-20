/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        int idx=0;
        stack<int> stk;
        vector<int> res;
        stack<int> idx_stk;
        ListNode* cur=head;
        while (cur != NULL) {
            while (!stk.empty() && stk.top() < cur->val) {
                res[idx_stk.top()] = cur->val;
                stk.pop();
                idx_stk.pop();
            }
            res.push_back(0);
            stk.push(cur->val);
            idx_stk.push(idx++);
            
            cur = cur->next;
        }
        return res;
    }
};
