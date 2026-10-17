# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle
        # head -> ...
        # slow -> fast
        slow = head
        fast = head.next
        # slow -> fast
        # head -> slow -> 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # weave the two halves together
        first, second = head, prev
        while second: 
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# time: O(n) 
# space: O(1) because the prompt said in-place wiring!          