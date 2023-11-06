class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isIdentical(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False

    return (
        node1.val == node2.val and
        isIdentical(node1.left, node2.left) and
        isIdentical(node1.right, node2.right)
    )

def containsTree(T1, T2):
    if not T2:
        # An empty tree is always contained in another tree
        return True

    if not T1:
        # T2 is not empty, but T1 is, so T1 cannot contain T2
        return False

    # If the current node in T1 matches the root of T2, check if T1 contains T2
    if T1.val == T2.val and isIdentical(T1, T2):
        return True

    # Otherwise, check recursively in the left and right subtrees of T1
    return containsTree(T1.left, T2) or containsTree(T1.right, T2)

# Example usage:
T1 = TreeNode(5)
T1.left = TreeNode(3)
T1.right = TreeNode(7)
T1.left.left = TreeNode(2)
T1.left.right = TreeNode(4)
T1.right.left = TreeNode(6)
T1.right.right = TreeNode(8)

T2 = TreeNode(3)
T2.left = TreeNode(2)
T2.right = TreeNode(4)

result = containsTree(T1, T2)
print(result)  # Output: True
