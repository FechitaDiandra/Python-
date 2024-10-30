class queue:
    def __init__(self):
        self.storage = []

    def push(self, *to_push):
        for i in to_push:
            self.storage.insert(0, i)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            return None

    def peek(self):
        if len(self.storage) > 0:
            return self.storage[len(self.storage) - 1]
        else:
            return None


q = queue()
q.push(1, 3, 6, 6.7)
print("peek:", q.peek())
q.push((4, 5))
print("popped:", q.pop())
print("peek:", q.peek())
print("popped:", q.pop())
print("popped:", q.pop())
print("popped:", q.pop())
print("popped:", q.pop())
print("popped:", q.pop())