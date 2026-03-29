# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        newRoot = TreeNode()

        if not root: 
            return root

        def invertRec(a, b):
            if not a: return
            # b = TreeNode()
            b.val = a.val
            if a.left: b.right = TreeNode(a.left.val)
            if a.right: b.left = TreeNode(a.right.val)
            print(b.val)
            invertRec(a.right, b.left)
            invertRec(a.left, b.right)


        newRoot.val = root.val
        invertRec(root, newRoot)

        return newRoot