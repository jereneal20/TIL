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
    int minimum=1000000000;
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        recurse(root, 1);
        return minimum;
    }
    void recurse(TreeNode *cur, int depth){
        if (cur == NULL) return;
        if (cur->right == NULL && cur->left == NULL) {
            minimum = min(depth, minimum);
            return;
        }
        recurse(cur->left, depth+1);
        recurse(cur->right, depth+1);
        return;
    }
};
