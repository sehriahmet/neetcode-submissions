# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check_same_tree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return check_same_tree(root.right, subRoot.right) and check_same_tree(root.left, subRoot.left)
            return False

        def dfs(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            if root.val == subRoot.val:
                return check_same_tree(root, subRoot) or dfs(root.right, subRoot) or dfs(root.left, subRoot)
            return dfs(root.right, subRoot) or dfs(root.left, subRoot)
            
        return dfs(root, subRoot)
