class stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self,val):
        if len(self.stack2) != 0:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(val)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return ('Empty Stacks', None)
        
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

s = stacks()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
        