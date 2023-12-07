


class Stack:
    def __init__(self):
        self._items = []
    
    def pop(self):
        return self._items.pop()
    def push(self, value):
        self._items.append(value)

    @property
    def top(self):
        return self._items[-1]
    
    @top.setter
    def top(self, value):
        self._items[-1] = value

    def __len__(self) -> int:
        return len(self._items)
    def empty(self) -> bool:
        return len(self) == 0