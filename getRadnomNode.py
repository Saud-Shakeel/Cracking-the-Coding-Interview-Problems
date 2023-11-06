import random

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def getRadnomBST(self, root, count):
        if not root:
            return None

        queue = [root]
        visited = [root]
        chosen_node = None

        while queue:
            node = queue.pop(0)            
            r = random.randint(0, count)
            
            if r == count:
                chosen_node = node
            count += 1

           
            if node.left and node.left not in visited:
                queue.append(node.left)
                visited.append(node.left)

            if node.right and node.right not in visited:
                queue.append(node.right)
                visited.append(node.right)

        return chosen_node

n = BST(5)
n1 = BST(-2)
n2 = BST(0)
n3 = BST(3)
n4 = BST(1)
n5 = BST(-5)

n.left = n1
n.right = n2
n1.left = n3
n2.left = n4
n2.right = n5

chosen_node = n.getRadnomBST(n, 0)
if chosen_node:
    print("Chosen Node Value:", chosen_node.val)
else:
    print("No node chosen.")
