class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def insert(self, n):
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

    def partition(self, ele):        
        small = self
        curr = self

        while curr.next:
            if curr.val >= ele:
                curr.val = curr.next.val
                curr.next = curr.next.next
            else:
                break

        while small.next:
            if small.next.val < ele:
                small = small.next
            else:
                break

        curr = small
        while curr.next:
            if curr.next.val < ele:
                new = Node(curr.next.val)
                new.next = small.next
                small.next = new
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        

m= Node(15)
m.insert(7)
m.insert(3)
m.insert(9)
m.insert(5)
m.insert(6)
m.insert(0)
m.insert(1)
m.insert(20)
m.display()
m.partition(5)
m.display()



