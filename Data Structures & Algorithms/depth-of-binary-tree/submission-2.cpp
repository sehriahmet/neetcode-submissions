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
    int max = 0;
    void dfs(TreeNode* curr, int depth) {
        if (!curr) {
            if (max < depth) max = depth;
        } else {
            dfs(curr->left, depth+1);
            dfs(curr->right, depth+1);
        }
    }
    int maxDepth(TreeNode* root) {
        dfs(root, 0);
        return max;
    }
};
