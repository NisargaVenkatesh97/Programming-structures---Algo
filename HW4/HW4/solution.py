
############################################################
# Write code in this file
# Post this file in Canvas
# Cut and paste the whole file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run this file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def add_last(self, val):
        new_node = ListNode(val)
        if not self._first:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def add_first(self, val):
        new_node = ListNode(val)
        if not self._first:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    def peek_first(self):
        return self._first.val if self._first else -1

    def peek_last(self):
        return self._last.val if self._last else -1
    

    def remove_first(self):
        if not self._first:
            return None

        val = self._first.val
        self._first = self._first.next
        self._len -= 1

        if not self._first:
            self._last = None

        return val
    
     def remove_last(self):
        if not self._first:
            return -1

        if self._first == self._last:
            val = self._first.val
            self._first = None
            self._last = None
            self._len -= 1
            return val

        current = self._first
        while current.next != self._last:
            current = current.next

        val = self._last.val
        current.next = None
        self._last = current
        self._len -= 1

        return val

    def is_empty(self):
        return self._len == 0
    
    def get_length(self):
        return self._len

  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    def push(self, x: int) -> None:
        self._s.add_first(x)

    def pop(self) -> int:
        return self._s.remove_first()

    def top(self) -> int
        return self._s.peek_first()

    def empty(self) -> bool:
        return self._s.is_empty()


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        self._s = Slist()
        
    def push(self, x):  
        self._s.add_last(x)

    def pop(self):  
        return self._s.remove_first()

    def peek(self):  
        return self._s.peek_first()

    def empty(self):  
        return self._s.is_empty()

############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
        
    def insertFront(self, value: int) -> bool:
        if self._s.get_length() < self._K:
            self._s.add_first(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self._s.get_length() < self._K:
            self._s.add_last(value)
            return True
        return False

    def deleteFront(self) -> bool:
        return self._s.remove_first() != -1

    def deleteLast(self) -> bool:
        return self._s.remove_last() != -1

    def getFront(self) -> int:
        return self._s.peek_first()

    def getRear(self) -> int:
        return self._s.peek_last()

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.get_length() == self._K
 

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.add_last(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s.remove_first()
        return True

    def Front(self) -> int:
        return self._s.peek_first()

    def Rear(self) -> int:
        return self._s.peek_last()

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.get_length() == self._K
    
    
    
 
