class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

    def insert(self,n):
        new = Node(n)
        curr = self
        while(curr.next):
            curr = curr.next
        curr.next = new
        new.prev = curr         
    
    def display(self):
        curr = self
        while(curr):
            print(curr.val, end=' -> ')
            curr = curr.next
        print('None')
    
disp = Node(4)
disp.insert(1)  
disp.insert(10)
disp.display()
disp.removeDuplicates()


