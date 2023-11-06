class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_loop_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c  

loop_start = find_loop_start(a)

if loop_start:
    print("Loop detected. Starting node of the loop:", loop_start.val)
else:
    print("No loop detected.")
