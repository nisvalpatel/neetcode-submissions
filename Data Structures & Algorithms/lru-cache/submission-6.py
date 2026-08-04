class LRUCache:
    
    class Node:
        def __init__(self,key = 0, val=0, next=None, prev=None):
            self.val = val
            self.next = next
            self.key = key
            self.prev = prev


    def __init__(self, capacity: int):
        self.count = 0.                 #this counts as 
        self.capacity = capacity
        self.head = self.Node()
        self.hashmap = defaultdict(lambda: -1)

        curr = self.head

        prev = None
        for i in range(capacity - 1):  #come back here when testing and it doesnt work properly
            curr.next = self.Node()
            curr.prev = prev
            prev = curr
            curr = curr.next
            
        
        curr.prev = prev
        curr.next = self.head
        self.head.prev = curr

        #basically made a cycle and the head pointer will just go around to update values.

        

    def get(self, key: int) -> int:

        if self.hashmap[key] == -1:
            return -1
        
        #remove this node from 
        tempNode = self.hashmap[key]
        self.put_to_back(tempNode)
        return self.hashmap[key].val

    def put_to_back(self, tempNode):
        if tempNode == self.head:
            self.head = self.head.next
        else:    
            tempNode.prev.next = tempNode.next
            tempNode.next.prev = tempNode.prev

            tempNode.prev = self.head.prev
            tempNode.next = self.head
            self.head.prev = tempNode
            tempNode.prev.next = tempNode
        

    def put(self, key: int, value: int) -> None:
        if self.count < self.capacity:
            if self.hashmap[key] == -1:
                self.head.key = key
                self.head.val = value
                self.hashmap[key] = self.head
                self.head = self.head.next
                self.count += 1
            else:
                self.hashmap[key].val = value
                self.put_to_back(self.hashmap[key])
            return
        
        if self.hashmap[key] == -1:
            temp = self.head.key
            self.hashmap[temp] = -1
            self.head.key = key
            self.head.val = value
            self.hashmap[key] = self.head
            self.head = self.head.next
            self.count += 1
        else:
            tempNode = self.hashmap[key]
            tempNode.val = value
            self.put_to_back(tempNode)
            self.count += 1




        
        
        
