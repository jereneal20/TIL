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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* odd = new ListNode(0), *odd_cur = odd;
        ListNode* even = new ListNode(0), *even_cur = even;
        ListNode* cur = head;
        int i= 0;
        while (cur != NULL) {
            i++;
            if (i % 2 == 0) {
                even_cur->next = cur;
                even_cur = even_cur->next;
            } else {
                odd_cur->next = cur;
                odd_cur = odd_cur->next;
            }
            cur = cur->next;
        }
        even_cur->next = NULL;
        odd_cur->next = even->next;
        return odd->next;
    }
};
