"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node 
        visited = []
        nodesMap = {} 
        newNode = Node(node.val) 
        nodesMap[node.val] = newNode 

        # newNode.neighbors.append(node.neighbors[0].val)
        def dfs(node, newNode):
            if len(node.neighbors) == 0 or node.val in visited: 
                return

            visited.append(node.val)

            nodesMap[node.val] = newNode 

            for i in range (len(node.neighbors)):
                if not node.neighbors[i].val in visited: 
                    newNode.neighbors.append(Node(node.neighbors[i].val))
                else: 
                    newNode.neighbors.append(nodesMap[node.neighbors[i].val])

                dfs(node.neighbors[i], newNode.neighbors[i])
            
        
        dfs(node, newNode)
        print(visited)
        return newNode
