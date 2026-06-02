"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Okay the strategy is to use a hash map such that every time
        # we build a node, we store the node in this hash map for easy
        # access. I will first make each node normal with the next feature
        # so it has the next pointer set while the random pointer for all
        # of them will be pointed to None. 

        dic = {}
        if head == None:
            return None
        temp_org = head
        curr = Node(head.val)
        head_ret = curr    #this will be my return value
        dic[head] = curr

        while head.next != None:
            temp = Node(head.next.val)
            dic[head.next] = temp
            curr.next = temp
            curr = curr.next
            head = head.next
        #this should set all the nodes into the hashmap. checked and it did

        curr = head_ret
        head = temp_org

        while head != None:
            random_og = head.random
            if random_og == None:
                curr.random = None
                curr = curr.next
                head = head.next
                continue
            curr.random = dic[random_og]
            curr = curr.next
            head = head.next


        return head_ret


        



