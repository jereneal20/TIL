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
    bool isCousins(TreeNode* root, int x, int y) {
        vector<int> res1,res2;
        if(root==NULL || root->val == x || root->val == y) return false;
        res1 = getParentAndDepth(root, x, 0);
        res2 = getParentAndDepth(root, y, 0);
        if (res1[0] == res2[0]) return false;
        if (res1[1] == res2[1]) return true;
        return false;
    }
    vector<int> getParentAndDepth(TreeNode* cur, int x, int depth) {
        vector<int> res;
        if (cur == NULL) return res;
        if ((cur->left != NULL && cur->left->val == x ) ||
            (cur->right != NULL && cur->right->val == x )){
            res.push_back(cur->val);
            res.push_back(depth+1);
            return res;
        }
        res = getParentAndDepth(cur->left, x, depth+1);
        if (!res.empty()) return res;
        res = getParentAndDepth(cur->right, x, depth+1);
        if (!res.empty()) return res;
        return res;
    }
};
