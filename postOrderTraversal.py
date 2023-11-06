class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def postOrder(self):
        if self:

            if self.left:
                self.left.postOrder()
            
            if self.right:
                self.right.postOrder()
            
            print(self.val)
            

n = node(8)
n1= node(6)
n2 = node(10)
n3 = node(4)
n4 = node(2)
n5 = node(20)

n.left = n1
n.right = n2
n1.left = n3
n3.left = n4
n2.right = n5

n.postOrder()