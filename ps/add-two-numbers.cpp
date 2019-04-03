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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* zero = new ListNode(0);
        ListNode* res = new ListNode(-1);
        ListNode* cur = res;
        bool carry = false;
        while (l1 || l2 || carry) {
            if (!l1) { l1 = zero;}
            if (!l2) { l2 = zero;}
            cur->next = new ListNode(l1->val + l2->val);
            cur = cur->next;
            cur->val += carry ? 1 : 0;
            carry = (cur->val >= 10) ? true : false;
            cur->val %= 10;
            l1 = l1->next;
            l2 = l2->next;
        }
        return res->next;
    }
};
