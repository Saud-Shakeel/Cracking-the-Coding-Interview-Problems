class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class bst_check:
    def __init__(self):
        pass

    def bst_check(self, root):
        if root:
            if root.left:
                if not self.bst_check(root.left):
                    return False
                if root.val < root.left.val:
                    return False
            
            if root.right:
                if not self.bst_check(root.right):
                    return False
                if root.val > root.right.val:
                    return False
      
        return True
       
n = node(10)
n1 = node(8)
n2 = node(12)
n3 = node(9)
n4 = node(11)
n5 = node(2)

n.left = n1
n.right = n2
n1.left = n5
n1.right = n3
n2.left = n4

b_tree = bst_check()
b_tree = b_tree.bst_check(n)
if b_tree:
    print(b_tree)
else:
    print(b_tree)