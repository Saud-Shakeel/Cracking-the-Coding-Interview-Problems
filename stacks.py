class stacks:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if not self.stack:
            return self.isEmpty()
        else:
            out = self.stack.pop()
            print(out)
            return out
    
    def isEmpty(self):
        if not self.stack:
            print('Empty Stack')

    def peek(self):
        if self.stack:
            top = self.stack[-1]
            print(top)
            return top
        else:
            self.isEmpty()

       

s = stacks()
s.push(9)
s.push(2)
s.peek()