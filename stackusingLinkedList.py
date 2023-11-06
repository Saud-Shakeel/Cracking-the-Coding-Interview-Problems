class Node:
    def __init__(self,val):
        self.next = None
        self.val = val


class stacks:
    def __init__(self):
       self.top = None
    
    def push(self,n):
        new = Node(n)
        new.next = self.top
        self.top = new
        print(self.top.val)  
    
    def pop(self):
        if self.top is None:
            return 'Empty Stack'
        popped_value = self.top.val
        self.top = self.top.next
        return popped_value

        

s = stacks()
s.push(1)
s.push(12)
print(s.pop())
print(s.pop())
print(s.pop())



        
