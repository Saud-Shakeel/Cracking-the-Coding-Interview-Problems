class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printSequences(self, arr1, arr2, results):
        arr1.append(self.val)
        arr2.append(self.val)

        is_leaf1 = not self.left and not self.right
        is_leaf2 = not self.left and not self.right

        if is_leaf1:
            results.append(arr1.copy())
        if is_leaf2:
            results.append(arr2.copy())

        if self.left:
            self.left.printSequences(arr1.copy(), arr2.copy(), results)
        if self.right:
            self.right.printSequences(arr1.copy(), arr2.copy(), results)

# Example usage:
root = Node(2)
root.left = Node(1)
root.right = Node(3)

sequences = []
root.printSequences([], [], sequences)

# Filter out duplicates and print the sequences
distinct_sequences = [list(set(seq)) for seq in sequences]
for seq in distinct_sequences:
    print(seq)

