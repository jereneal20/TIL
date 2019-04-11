/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    stack<TreeNode*> stk;
    BSTIterator(TreeNode* root) {
        TreeNode* cur=root;
        while(cur!=NULL) {
            stk.push(cur);
            cur = cur->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode* cur = stk.top();
        int ret = cur->val;
        stk.pop();
        if (cur->right){
            cur = cur->right;
            while (cur != NULL) {
                stk.push(cur);
                cur = cur->left;
            }
        }
        return ret;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        if (stk.size() == 0) return false;
        else return true;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
