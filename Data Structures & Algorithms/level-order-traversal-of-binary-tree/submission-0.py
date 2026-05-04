# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] 
        result = [[]]

        def rec(node, n):
            nonlocal result
            if not node: return 
            if len(result) <= n:
                result.append([])
            result[n].append(node.val)
            rec(node.left, n+1)
            rec(node.right, n+1)
        rec(root, 0)
        return result
        