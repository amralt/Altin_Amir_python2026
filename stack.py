
class Stack():
    def __init__(self):
        self._list = list()

    def push(self: Stack, n: int):
        self._list.append(n)

    def pop(self: Stack):
        if len(self._list) == 0:
            raise Exception("Попытка взять элемент из пустого списка")
        
        return self._list.pop(-1)

    def peek(self: Stack) -> int:
        if len(self._list) == 0:
            raise Exception("Попытка взять элемент из пустого списка")
        
        return self._list[-1]

    def __len__(self):
        return len(self._list)
    
    def __bool__(self):
        return len(self._list) != 0

    def __contains__(self, item):
        return item in self._list
        
    def __repr__(self):
        return f"Stack({self._list})"
    

s = Stack()
for i in range(10):
    s.push(i)

print(s)
s.pop()
print(s)
print(f"in: {4 in s}")
print(f"peek: {s.peek()}")

