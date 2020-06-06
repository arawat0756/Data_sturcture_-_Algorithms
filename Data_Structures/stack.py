from exceptions import Empty
class ArrayStack:
    '''The Stack works on LIFO(Last In First Out).'''
    def __init__(self):
        self._data = []
    
    def __len__(self):
        '''Return len of array'''
        return len(self._data)
    
    def is_empty(self):
        '''To check the arrray is empty or not'''
        return len(self._data) == 0
    
    def push(self, e):
        '''push or append value in array'''
        self._data.append(e)
        
    def pop(self):
        '''remove valuue from the end'''
        if self.is_empty():
            raise Empty('Array is empty')
        return self._data.pop()
        
    def top(self):
        '''check top value of array'''
        if self.is_empty():
            raise Empty('Array is empty')
        return self._data[-1]

s = ArrayStack()
s.push(10)
s.push(20)
print("Stack : ", s._data)
print('Length : ', len(s))
print('Is-Empty : ', s.is_empty())
print('Popped : ', s.pop())
print('Stack : ', s._data)
print('Popped : ', s.pop())
print('Is-Empty : ', s.is_empty())
print('Stack : ', s._data)
s.push(30)
s.push(40)
print('Top Element : ', s.top())
