class graph:
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

node1 = graph(1)
node2 = graph(2)
node3 = graph(3)
node4 = graph(4)
node5 = graph(5)
node6 = graph(6)

node1.children = [node2, node3, node4]
node2.children = [node3]
node4.children = [node5, node6, node1]
node5.children = [node6]

dfs = depthFirstSearch()
dfs.dfs(node4, [])
