class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sumPaths(node, dist, current_sum):
    count = 0

    if node:
        new_sum = node.val + current_sum

        l_count = sumPaths(node.left, dist, new_sum)
        r_count = sumPaths(node.right, dist, new_sum)

        if new_sum == dist: 
            count +=1
            return count
        else:
            return l_count + r_count 
    else:
        return 0
        
def preOrder(node, dist):
    if node:
        l = preOrder(node.left, dist)
        r = preOrder(node.right, dist)
        c = sumPaths(node, dist, 0)

        return l + r + c
    else:
        return 0

n = Node(1)
n1 = Node(2)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)
n5 = Node(0)
n6 = Node(6)

n.left = n1
n.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
n2.left = n6

print(preOrder(n, 6))
