class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
    def preOrder(self):
        if self:
            print(self.val)
            if self.left:
                self.left.preOrder()
                
            if self.right:
                self.right.preOrder()

        
        
n = node(8)
n1 = node(6)
n2 = node(10)
n3 = node(2)
n4 = node(4)
n5 = node(20)

n.left = n1
n.right = n2
n1.left = n4
n4.left = n3
n2.right = n5

n.preOrder()


    
