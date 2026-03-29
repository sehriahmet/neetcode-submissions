"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes = {}
        nodesIndex = {}
        curr = head
        
        i=0
        while curr:
            newNode = Node(curr.val)
            newNodes[i] = newNode
            nodesIndex[curr] = i
            curr = curr.next
            i+=1
        curr = head
        i=0
        while curr:
            newNode = newNodes[i]
            if curr.next: newNode.next = newNodes[nodesIndex[curr.next]]
            if curr.random: newNode.random = newNodes[nodesIndex[curr.random]]
            curr = curr.next
            i+=1
        return newNodes[0] if newNodes else None