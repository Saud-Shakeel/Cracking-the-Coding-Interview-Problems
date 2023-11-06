class graph:
    def __init__(self,val):
        self.val = val
        self.children = []
    
class breadthFirstSearch:
    def __init__(self):
        pass

    def bfs(self,node, visited):
        queue = []
        queue.append(node)
        visited.append(node)

        while queue:
            n= queue.pop(0)
            print(n.val)
            for child in n.children:
                if child not in visited:
                    queue.append(child)
                    visited.append(child)

node1 = graph(1)
node2 = graph(2)
node3 = graph(3)
node4 = graph(4)
node5 = graph(5)
node6 = graph(6)

node1.children = [node2, node3, node6]
node2.children = [node5]
node4.children = [node5, node6, node1]
node5.children = [node6]

bfs = breadthFirstSearch()
bfs.bfs(node1, [])
