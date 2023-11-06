class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class balancedTree:
    def __init__(self):
        pass

    def check_tree(self, root):
        if root:

            if root.left:
                l_count, l_bal = self.check_tree(root.left)
            else:
                l_count, l_bal = (0,True)


            if root.right:
                r_count, r_bal = self.check_tree(root.right)
            else:
                r_count, r_bal = (0,True)

            
            if l_bal and r_bal:
                if abs(l_count - r_count) > 1:
                    return (l_count+r_count+1, False)
                else:
                    return (l_count+r_count+1, True)
                
                
        else:
            return (0, True)

n = node(10)
n1 = node(7)
n2 = node(12)
n3 = node(8)
n4 = node(11)
n5 = node(4)

n.left = n1
n.right = n2
# n1.left = n5
n1.right = n3
# n2.left = n4

bal = balancedTree()
count, balance = bal.check_tree(n)
if balance:
    print(count,balance)
else:
    print(count, balance)