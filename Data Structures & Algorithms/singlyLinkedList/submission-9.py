class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if self.size == 0 or self.size <= index:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        if temp is not None:
            return temp.val
        return -1

    def insertHead(self, val: int) -> None:
        temp = Node()
        temp.val = val

        if self.size == 0:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
            
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        temp = Node()
        temp.val = val

        if self.size == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size == 0 or index >= self.size:
            return False
        temp = self.head

        if index == 0:   #accounting for index 0 being removed
            self.head = temp.next
            temp = None
            self.size -= 1
            return True

        for i in range(index - 1):  
            temp = temp.next

        if index == self.size - 1:  #accounting for last element
            temp.next = None
            self.tail = temp
            self.size -= 1
            return True   

        left = temp 
        left.next = temp.next.next
        self.size -= 1
        return True

        

    def getValues(self) -> List[int]:
        temp_arr = []
        temp = self.head
        for i in range(self.size):
            temp_arr.append(temp.val)
            temp = temp.next
        return temp_arr
        
