class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SortedBST:
    def __init__(self):
        pass

    def minimalBST(self, l):
        if len(l) == 1:
            return Node(l[0])
        if len(l) == 0:
            return None
        
        sortedArr = sorted(l)
        mid = len(sortedArr) // 2
        n = Node(sortedArr[mid])
        
        n.left = self.minimalBST(sortedArr[:mid])
        n.right = self.minimalBST(sortedArr[mid+1:])
        return n
    
    def printBSTInOrder(self, root):
        if root:
            self.printBSTInOrder(root.left)
            print(root.val)
            self.printBSTInOrder(root.right)

sort = SortedBST()
root = sort.minimalBST([10, 12, 1, 0, 4, 6, 9, 3])
sort.printBSTInOrder(root)
