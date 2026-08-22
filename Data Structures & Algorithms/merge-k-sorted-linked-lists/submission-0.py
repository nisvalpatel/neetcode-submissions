# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []     #(value, list index, value index in list)

        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        head = None
        if heap != []:
            
            temp = heapq.heappop(heap)
            head = temp[2]
            index = temp[1]
            curr = head
            next = curr.next
            if next != None:
                heapq.heappush(heap, (next.val, index, next))
        
        while heap != []:
            temp_tuple = heapq.heappop(heap)
            temp = temp_tuple[2]
            index = temp_tuple[1]
            next = temp.next
            if next != None:
                heapq.heappush(heap, (next.val, index, next))
            curr.next = temp
            curr = curr.next
        
        return head






