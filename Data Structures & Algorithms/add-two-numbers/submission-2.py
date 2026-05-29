# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 5 
        # 9 5 6 
        # 0 8 9
        # check whether if it is last digit 

        temp = ListNode()
        result = temp
        carry = 0 

        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                carry = res // 10
                res1 = res % 10 
            else:
                carry = 0
                res1 = res
            temp.next = ListNode(res1)

            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = l1.val + carry
            if res >= 10:
                carry = res // 10
                res1 = res % 10 
            else:
                carry = 0
                res1 = res
            temp.next = ListNode(res1)
            l1 = l1.next
            temp = temp.next

        while l2:
            res = l2.val + carry
            if res >= 10:
                carry = res // 10
                res1 = res % 10 
            else:
                carry = 0
                res1 = res
            temp.next = ListNode(res1)
            l2 = l2.next
            temp = temp.next
        
        if carry > 0: 
            temp.next = ListNode(carry)
        
        return result.next if result else result
