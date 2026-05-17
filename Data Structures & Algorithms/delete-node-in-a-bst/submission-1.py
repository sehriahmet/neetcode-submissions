# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def update_subtree(curr): # curr is the key node 
            subroot = curr.right
            if not subroot: 
                return curr.left

            # find left_node rightmost node. 
            temp = curr.left 
            while temp and temp.right != None:
                temp = temp.right
            
            if temp:
                temp.right = subroot.left 
                subroot.left = curr.left                

            return subroot 
        
        if root.val == key:
            return update_subtree(root)
        
        # find the key node 
        temp = root
        prev = root
        while temp != None:
            if temp.val == key:
                if prev.val > key:
                    prev.left = update_subtree(temp)
                else:
                    prev.right = update_subtree(temp)
                return root
            
            prev = temp 
            if temp.val > key:
                temp = temp.left 
            else: 
                temp = temp.right
        return root

            