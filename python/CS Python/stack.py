class stack:
    def __init__(self, data):
        self.stack = []
        for x in list(data):
            self.stack.append(x)

    def isEmpty(self):
        return not bool(self.stack[0])
        
    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.stack[len(self.stack) - 1]
            
    def pop(self):
        if self.isEmpty():
            print('No entries to remove')
        else:
            self.stack.pop(len(self.stack) - 1)

    def push(self, entry):
        self.stack.append(entry)



x = stack((2, 'list', True))
print(x.peek(), x)
x.push('list2')
print(x.peek())
x.pop()
print(x.stack)