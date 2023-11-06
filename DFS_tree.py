class tree:
    def __init__(self,val):
        self.val = val
        self.children = []

class depthFirstSearch:
    def __init__(self):
       pass

    def dfs(self,node, visited):
        if node is None:
            return None
    
        print(node.val)
        visited.append(node)
        
        for child in node.children:
            if child not in visited:
                self.dfs(child, visited)

node1 = tree(1)
node2 = tree(2)
node3 = tree(3)
node4 = tree(4)
node5 = tree(5)
node6 = tree(6)
node7 = tree(7)
node8 = tree(8)

node1.children = [node2, node3]
node2.children = [node6]
node3.children = [node4, node5]
node6.children = [node7, node8]

dfs = depthFirstSearch()
dfs.dfs(node1, [])
