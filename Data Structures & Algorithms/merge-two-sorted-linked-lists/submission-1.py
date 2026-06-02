# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # to save space. i will basically just parse through
        # these two and make the solution array equal to list1
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None

        top = list1
        bottom = list2
        
        if top.val > bottom.val:
            ret = bottom
            bottom = bottom.next
        else:
            ret = top
            top = top.next

        temp = ret        
    
        
        while top != None and bottom != None:

            if top.val > bottom.val:
                ret.next = bottom
                bottom = bottom.next
            else:
                ret.next = top
                top = top.next
            ret = ret.next
        
        if top == None:
            ret.next = bottom
        elif bottom == None:
            ret.next = top

        return temp
            




                
                
         