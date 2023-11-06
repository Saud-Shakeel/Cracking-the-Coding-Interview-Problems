class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class commonAncestor:
    def __init__(self):
        pass

    def find_ancestor(self, node, x, y):
        if node is None:
            return (False, None)

        l_found, l_node = self.find_ancestor(node.left, x, y)
        r_found, r_node = self.find_ancestor(node.right, x, y)

        if node == x or node == y:
            return (True, node)

        if l_found and r_found:
            return (True, node)

        if l_found:
            return (True, l_node)

        if r_found:
            return (True, r_node)

        return (False, None)

n = treeNode(1)
n1 = treeNode(2)
n2 = treeNode(3)
n3 = treeNode(4)
n4 = treeNode(5)
n5 = treeNode(6)
n6 = treeNode(7)
n7 = treeNode(8)
n8 = treeNode(9)
#     1
#     /\
#   2    3
#  /\    /\
# 4 5   6  7
#          /\
#         8  9   
n.left = n1                                   
n.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n6.left = n7
n6.right = n8

com = commonAncestor()
bool, value  = com.find_ancestor(n, n3, n4)
print(bool,value.val)