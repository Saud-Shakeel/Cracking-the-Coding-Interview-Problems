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

    def palindrome(self):
        curr = self
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next
        if arr == arr[::-1]:
            print("is_palindrome")
        else:
            print("not_palindrome")



m  = Node('a')
m.insert('b')
m.insert('b')
m.insert('c')
m.insert('a')
m.display()
m.palindrome()