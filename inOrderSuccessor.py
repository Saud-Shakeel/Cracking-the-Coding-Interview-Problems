class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def find_in_order_successor(node):
    if node is None:
        return None

    if node.right:
        return find_min(node.right)
    
    else:
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

def find_min(node):
    while node.left:
        node = node.left
    return node

root = TreeNode(10)
n1 = TreeNode(8)
n2 = TreeNode(12)
n3 = TreeNode(9)
n4 = TreeNode(11)
n5 = TreeNode(2)

root.left = n1
root.right = n2
n1.parent = root
n2.parent = root
n5.parent = n1
n3.parent = n1
n4.parent = n2

s = find_in_order_successor(root)

if s:
    print(s.val)
else:
    print("No in-order successor (root node)")
