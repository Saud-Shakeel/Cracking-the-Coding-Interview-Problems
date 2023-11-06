class stacks:
    def __init__(self):
        self.stack = []
        self.min_ele = float('inf')

    def push(self,val):
        if val < self.min_ele:
           self.min_ele = val
        self.stack.append((val,self.min_ele))
    
    def pop(self):
        if not self.stack:
            return self.isEmpty()
        else:
            out = self.stack.pop()
            if out[1] == self.min_ele:
                self.min_ele = float('inf')
            print(out)
            return out
        
    def minimum(self):
        if not self.stack:
            print('Empty Stack')
        else:
            m = self.stack[-1][1]
            print(m)
            return m

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
s.push(2)
s.push(3)
s.push(4)
s.push(1)
s.push(5)
s.push(0)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.minimum()

