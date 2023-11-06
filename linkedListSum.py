class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def display(self):
        curr = self
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print('None')
    
    def sum(self, l1, l2):
        # carry = 0
        # new_head = Node(0)
        # curr = new_head
        # while l1 or l2:
        #     if l1 or l2:
        #         val = l1.val + l2.val + carry
        #         l1 = l1.next                
        #         l2 = l2.next
        #     if val > 9:
        #         carry = val // 10
        #         val %= 10
        #     curr.next = Node(val)
        #     curr = curr.next
        # return new_head.next
        carry = 0
        stack1 = []
        stack2 = []
        new_head = Node(0)
        curr = new_head
        while l1 or l2:
            stack1.append(l1.val)
            l1 = l1.next  
            stack2.append(l2.val)          
            l2 = l2.next
        
        while stack1 or stack2:
            if stack1 or stack2:
                val = stack1.pop() + stack2.pop() + carry
            if val >9:
                carry //= 10
                val %= 10
            curr.next = Node(val)
            curr = curr.next
        return new_head.next

           
        
m = Node(2)
m1 = Node(1)
m2 = Node(6)
m.next = m1
m1.next = m2

n = Node(5)
n1 = Node(8)
n2 = Node(2)
n.next = n1
n1.next = n2

res = Node(0)
res = res.sum(m,n)
res.display()

