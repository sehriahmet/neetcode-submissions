/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool check_rec(TreeNode* curr, int min, int max) {
        if (!curr) return true;
        if (curr->left && (curr->left->val >= curr->val || curr->left->val <= min)) {
            return false;
        }
        if (curr->right && (curr->right->val <= curr->val || curr->right->val >=max)) {
            return false;
        }
        return (check_rec(curr->left, min, curr->val)
                && check_rec(curr->right, curr->val, max));
    }
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        return check_rec(root, INT_MIN, INT_MAX);
    }
};
