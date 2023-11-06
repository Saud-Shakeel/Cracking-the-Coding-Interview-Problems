# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.fast = None
    
#     def insert(self, n):
#         new = Node(n)
#         curr = self
#         while(curr.fast):
#             curr = curr.fast
#         curr.fast = new
    
#     def display(self):
#         curr = self
#         while(curr):
#             print(curr.val, end=' -> ')
#             curr = curr.fast
#         print('None')
    

#     def kLastElement(self, k):
#         curr = self
#         count = 0
#         while(curr):
#             curr = curr.fast
#             count +=1

#         curr = self
#         k_element = count - k

#         while(k_element > 0):
#             curr = curr.fast
#             k_element -=1 
#         print('Kth Last Element:',curr.val)


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

    def kLastElement(self,k):
        fast = self
        slow = self

        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        print(slow.val)  



m = Node(3)
m.insert(1)
m.insert(10)
m.insert(7)
m.insert(9)
m.display()
m.kLastElement(3)
