from exceptions import Empty

class LinkedStack:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size = self._size + 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        value = self._head._element
        self._head = self._head._next
        self._size = self._size -1
        return value
    
    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._head._element
    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end="-->")
            temp = temp._next
        print()
        
l = LinkedStack()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.display()
print('Popped : ', l.pop())
l.display()
l.push(70)
l.display()
print("Top Element : ", l.top())
print('Pooped : ', l.pop())
l.display()





        