# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_map = {}
        visited = set()
        def dfs(node, level):
            if not node or node.val in visited: 
                return 
            if level not in level_map:
                level_map[level] = [node.val]
            else: 
                level_map[level].append(node.val)
            visited.add(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)

        result = []
        for level in level_map:
            result.append(level_map[level][-1])

        return result
