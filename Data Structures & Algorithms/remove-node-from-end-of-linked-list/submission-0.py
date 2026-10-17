# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length == n:                     # the target IS the head
            return head.next                # just drop it

        curr = head                         # reset, starting at head
        for i in range(length - n - 1):     # one fewer step: stop BEFORE the target
            curr = curr.next
        curr.next = curr.next.next
        return head