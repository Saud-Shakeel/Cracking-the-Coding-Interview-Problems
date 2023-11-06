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

    def deleteNode(self):
        self = self.next.next
        curr = self
        curr.val = curr.next.val
        curr.next = curr.next.next


    
m = Node('a')
m.insert('b')
m.insert('c')
m.insert('d')
m.insert('e')
m.insert('f')
m.display()
m.deleteNode()
m.display()