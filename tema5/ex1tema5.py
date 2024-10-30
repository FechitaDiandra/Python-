class stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def push(self, *to_push):
        for i in to_push:
            self.storage.append(i)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            temp = self.storage[self.size]
            self.storage.pop(self.size)
            return temp
        else:
            return None

    def peek(self):
        if self.size > 0:
            return self.storage[self.size - 1]
        else:
            return None


stk = stack()
stk.push(1, 3, 6, 6.7)
print("peek:", stk.peek())
stk.push((4, 5))
print("peek:", stk.peek())
print("popped:", stk.pop())
print("peek:", stk.peek())
print("popped:", stk.pop())
print("popped:", stk.pop())
print("popped:", stk.pop())
print("popped:", stk.pop())
print("popped:", stk.pop())