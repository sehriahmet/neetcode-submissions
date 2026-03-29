# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        curr = head 
        flag = 0
        while curr:
            if len(result) < n+1:
                result.append(curr)
            else:
                result.pop(0)
                result.append(curr)
                print("second if")
                if curr.next == None:
                    prev = result[0]
                    print(prev.val, len(result))
                    prev.next = prev.next.next
                    flag = 1
            curr = curr.next
        if not flag:
            print(len(result), n)
            if n == len(result):
                if len(result) > 1: head = result[1]
                else: head = None
            else: 
                prev = result[0]
                prev.next = prev.next.next
        return head