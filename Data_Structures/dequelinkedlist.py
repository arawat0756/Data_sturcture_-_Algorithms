from exceptions import Empty

class LinkedDeque:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self,e):
            newest = self._Node(e, None)
            if self.is_empty():
                self._head = newest
                self._tails = newest
            else:
                newest._next = self._head
            self._head = newest
            self._size += 1

    def add_last(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty("Linked list empty")
        value = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty():
            self._tail = None
        return value
    
    def remove_last(self):
        if self.is_empty():
            raise Empty("Linked list empty")
        thead = self._head
        i = 0
        while i < len(self)-2:
            thead = thead._next
            i += 1
        self._tail = thead
        thead = thead._next
        value = thead._element
        self._tail._next = None
        self._size -= 1
        return value

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end='-->')
            thead = thead._next
        print()

l = LinkedDeque()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)
l.display()
print("Deleted : ", l.remove_first())
l.display()
l.add_first(70)
l.display()
print('Deleted : ', l.remove_last())
l.display()


            
            