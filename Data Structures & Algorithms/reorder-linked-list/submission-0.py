# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find the middle (slow ends at midpoint)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse the second half
        second = slow.next
        slow.next = None          # split the list into two halves
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev is now the head of the reversed second half

        # Step 3: merge the two halves, alternating nodes
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
