class stacks:
    def __init__(self):
        self.threshold = 3
        self.stacks = []
    
    def push(self,val):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.threshold:
            s = []
            self.stacks.append(s)
        self.stacks[-1].append(val)

    def pop(self):
        if len(self.stacks)==0:
            return 'Empty Stacks'
        
        if not self.stacks[-1]:
            self.stacks.pop()    
        return self.stacks[-1].pop()
    
s = stacks()
s.push(1)
s.push(2)
s.push(3)
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
print(s.pop())

        