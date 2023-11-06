class tree:
    def __init__(self,val):
        self.val = val
        self.children = []
    
class breadthFirstSearch:
    def __init__(self):
        pass

    def bfs(self, node, visited):
        queue = []
        queue.append(node)
        
        while queue:
            n = queue.pop(0)
            print(n.val)

            for child in n.children:
                if child not in visited:
                    queue.append(child)
                    visited.append(child)


node1 = tree(1)
node2 = tree(2)
node3 = tree(3)
node4 = tree(4)
node5 = tree(5)
node6 = tree(6)
node7 = tree(7)
node8 = tree(8)

node1.children = [node2, node3]
node2.children = [node6, node8]
node3.children = [node4, node5]
node6.children = [node7]

bfs = breadthFirstSearch()
bfs.bfs(node1, [])