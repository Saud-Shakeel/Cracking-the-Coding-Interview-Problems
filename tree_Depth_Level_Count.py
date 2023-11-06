class depthOfTree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def levelCounts(self, root, level):
        if not root:
            return level

        max_child_depth = level
        for child in root.children:
            child_depth = self.levelCounts(child, level + 1)
            max_child_depth = max(max_child_depth, child_depth)

        return max_child_depth

n = depthOfTree(10)
n1 = depthOfTree(1)
n2 = depthOfTree(0)
n3 = depthOfTree(6)
n4 = depthOfTree(9)
n5 = depthOfTree(12)

n.children = [n1, n2]
n1.children = [n3, n4]
n2.children = [n5]

res = n.levelCounts(n, 0)
print(res)
