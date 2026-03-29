# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search_tree(root, left_bound, right_bound):
            if not root: return True 
            print(root.val, left_bound, right_bound)
            if root.val <= left_bound or root.val >= right_bound: return False
            return search_tree(root.left, left_bound, root.val) and search_tree(root.right, root.val, right_bound)
            
        return search_tree(root, float("-inf"), float("inf"))