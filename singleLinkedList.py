class Node:
    def __init__(self, val):
        self.val = val
        self.next=None

    def insert(self, n):
        new = Node(n)
        curr = self
        while(curr.next):
            curr = curr.next
        curr.next = new

    def retrieve(self, v):
        curr = self
        while(curr):
            if curr.val == v:
                print(curr.val)
            curr = curr.next

    def removal(self,rem):
        curr = self
        while(curr.next):
            if curr.next.val == rem:
                curr.next = curr.next.next
                continue
            curr = curr.next
    

    def removeDuplicates(self):
        curr = self
        dictt = {}
        while(curr.next):
            if curr.next.val in dictt:
                curr.next = curr.next.next
                continue
            else:
                dictt[curr.next.val] = 1
            curr= curr.next


    def display(self):
        curr  = self
        while(curr):
            print(curr.val, end=' -> ')
            curr = curr.next
        print('None')

node = Node(1)
node.insert(8)
node.insert(2)
node.insert(10)
node.insert(6)
node.insert(6)
node.insert(10)
node.insert(3)
node.insert(7)

node.display()
node.removeDuplicates()
node.display()
