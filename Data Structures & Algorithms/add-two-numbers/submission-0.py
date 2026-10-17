# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toNumber(node):
            stack = []
            while node:
                stack.append(str(node.val))
                node = node.next
            digits = ""
            while stack:
                digits += stack.pop()
            return int(digits)
        
        total = toNumber(l1) + toNumber(l2)          

        # build the answer in reverse order: 7 → 0 → 8
        dummy = tail = ListNode()
        for d in reversed(str(total)):               
            tail.next = ListNode(int(d))
            tail = tail.next
        return dummy.next
