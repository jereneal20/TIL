/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* cur=head, *head2, *tmp;
        if (head==NULL) return NULL;
        while(cur!=NULL) {
            cur->next = new Node(cur->val, cur->next, cur->random);
            cur = cur->next->next;
        }
        head2 = head->next;
        cur=head->next;
        while(cur!=NULL) {
            if (cur->random != NULL)
                cur->random = cur->random->next;
            if (cur->next == NULL) break;
            cur = cur->next->next;
        }
        cur=head;
        while(cur!=NULL) {
            if (cur->next == NULL) break;
            tmp = cur->next;
            cur->next = cur->next->next;
            cur = tmp;
        }
        return head2;
    }
};
