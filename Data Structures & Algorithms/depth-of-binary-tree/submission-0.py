# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = set()
        result = set() 
        def dfs(node, n):
            if not node:
                result.add(n)
                return 
            if node in visited: return 
            visited.add(node)
            dfs(node.left, n+1)
            dfs(node.right, n+1)
        dfs(root, 0)
        return max(result)  