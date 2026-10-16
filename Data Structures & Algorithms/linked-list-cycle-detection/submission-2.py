# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        while fast and fast.next:
            # fast gains exactly 1 node on slow per step, so it can’t jump over slow.
            # basically any pair speeds differ exactly by 1
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False