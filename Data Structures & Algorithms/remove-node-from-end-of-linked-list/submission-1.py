# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #I think I will optimize

        if head == None:
            return None

        fast_curr = head

        for i in range(n):
            fast_curr = fast_curr.next
            if fast_curr == None:
                return head.next
        
        slow_curr = head

        while fast_curr.next != None:
            fast_curr = fast_curr.next
            slow_curr = slow_curr.next
    

        slow_curr.next = slow_curr.next.next

        return head
        

