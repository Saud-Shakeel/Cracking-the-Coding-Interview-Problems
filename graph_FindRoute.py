class graph:
    def __init__(self, val):
        self.val = val
        self.children = []

class route:
    def __init__(self):
        pass

    # def breadthFirstSearch(self, sNode, eNode):
    #     queue = []
    #     visited = []
    #     queue.append(sNode)

    #     while queue:
    #         n = queue.pop(0)
    #         if n.val == eNode.val:
    #             print('Both at the same node:', n.val)
    #             return True
    #         for child in n.children:
    #             if child not in visited:
    #                 queue.append(child)
    #                 visited.append(child)
    #                 if child == eNode:
    #                     print('Route Available')
    #                     return True

    #     print('Route Not Available')
    #     return False

    def depthFirstSearch(self, sNode, eNode, visited):
        visited.append(sNode)

        for child in sNode.children:
            if child not in visited:
                if self.depthFirstSearch(child, eNode, visited):
                    return True

        if sNode.val == eNode.val:
            return True

        return False
    

node0 = graph(-1)
node1 = graph(0)
node2 = graph(1)
node3 = graph(2)
node4 = graph(3)
node5 = graph(4)
node6 = graph(6)

node0.children = [node1, node4, node6]
node1.children = [node2]
node2.children = [node1]
node3.children = [node2, node4]
node4.children = [node3]

r = route()
result = r.depthFirstSearch(node0, node6, [])
if result:
    print('Route Available')
else:
    print('Route Not Available')