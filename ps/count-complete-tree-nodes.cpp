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
    int getDepth(TreeNode* root) {
        int i=-1;
        while (root) {
            root = root->left;
            i++;
        }
        return i;
    }
    bool existElement(TreeNode* root, int depth, int idx) {
        TreeNode* cur = root;
        int leafIdx = idx - pow(2, depth);
        depth--;
        while (depth >= 0) {
            if (!cur) return false;
            if (1 << depth & leafIdx) {
                cur = cur->right;
            } else {
                cur = cur->left;
            }
            depth--;
        }
        if (!cur) return false;
        return true;
    }
    int countNodes(TreeNode* root) {
        int depth = getDepth(root);
        int start = pow(2, depth), end = pow(2, depth+1)-1, mid;
        int res = 0;
        while (start <= end){
            mid = (start+end)/2;
            if (existElement(root, depth, mid)) {
                res = mid;
                start = mid + 1;
            }else {
                end = mid - 1;
            }
            if (start > end) break;
        }
        return res;
    }
};
