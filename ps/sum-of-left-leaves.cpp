/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sum;
    int sumOfLeftLeaves(TreeNode* root) {
        sum = 0;
        recurse(root);
        return sum;
    }
    void recurse(TreeNode* cur) {
        if (cur == NULL) return;
        if (cur->left != NULL){
            if ( cur->left->left == NULL && cur->left->right == NULL) {
                // cout << cur->val << endl;
                sum += cur->left->val;
            }
        } 
        recurse(cur->left);
        recurse(cur->right);
        return;
    }
};
