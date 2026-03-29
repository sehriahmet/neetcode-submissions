# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder_traverse(i, j):
            if i != None and j != None and i.val != j.val: 
                return False

            if i == None and j == None: 
                return True 
            if (i == None and j != None) or (i != None and j == None):
                return False
            if i.val == j.val:
                print(i.val, j.val)
                return inorder_traverse(i.left, j.left) and inorder_traverse(i.right, j.right)
        return inorder_traverse(p, q)