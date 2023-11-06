class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


    def buildOrder(self, d1):
        visited = []
        output = []    

        # Perform DFS starting from nodes with no incoming edges
        for node in d1:
            if node.val not in visited:
                self.dfs(node)

        # Check if all nodes are included in the build order
        for node in d1:
                if node.children and node not in output:
                    return "Error: No valid build order exists."

        return output[::-1]

    def dfs(self, node):
        visited = []
        output = []
        visited.append(node)
        for child in node.children:
            if child not in visited:
                self.dfs(child)
        output.append(node.val)     

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.children = [d]
f.children = [b, a]
b.children = [d]
d.children = [c]

projects = [a, b, c, d, e, f]
result = f.buildOrder(projects)
print(result)
