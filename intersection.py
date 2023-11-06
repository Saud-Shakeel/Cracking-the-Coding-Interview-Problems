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

    def intersection(self, l1, l2):
        dictt = {}
        p1 = l1
        p2 = l2

        while p1:
            dictt[p1] = p1
            p1 = p1.next

        while p2:
            if p2 in dictt.values():
                return (True, p2.val)
            p2 = p2.next
        return (False, None)

n = Node('j')
n1 = Node('l')
n2 = Node('k')
n3 = Node('a')
n4 = Node('b')
n5 = Node('c')
n.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

k = Node('x')
k1 = Node('l')  
k2 = Node('k')  
k3 = n3
k4 = n4
k5 = n5
k.next = k1
k1.next = k2
k2.next = k3
k3.next = k4
k4.next = k5

result, intersected_val = k.intersection(n, k)
print(result, intersected_val)

n.display()
k.display()
