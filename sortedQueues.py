class sorted_stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self,val):
        while(self.stack1):
            if self.stack1[-1] < val:
                self.stack2.append(self.stack1.pop())
            else:
                break
        self.stack1.append(val)
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        
    def pop(self):
        if not self.stack1:
            return 'Empty Stack'
        return self.stack1.pop()
    
    def peek(self):
        if not self.stack1:
            return 'Empty Stack'
        return self.stack1[-1]
    
s =sorted_stacks()
s.push(3)
s.push(10)
s.push(9)
s.push(4)
print(s.pop())
print(s.pop())
print(s.peek())
