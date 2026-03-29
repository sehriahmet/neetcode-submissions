# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def subLastNode(head):
            curr = head  
            while curr.next != None and curr.next.next != None:
                curr = curr.next
            lastNode = curr.next
            curr.next = None
            return lastNode
        
        def countList(head):
            curr = head  
            i = 1
            while curr.next != None:
                curr = curr.next
                i += 1 
            return i

        if head == None or head.next == None:
            return
        i=0
        curr = head
        n = countList(head) 
        # print(int(n/2))
        for iteration in range(int(n/2)):
            temp = curr.next 
            if temp.next: 
                curr.next = subLastNode(head)
                curr.next.next = temp 
                curr = curr.next.next
            # print(curr.next.val, curr.next.next.val, curr.next.next.next.val)


        