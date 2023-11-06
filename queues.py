class queues:
    def __init__(self):
        self.queue = []
    
    def enqueu(self,val):
        self.queue.append(val)
    
    def dequeu(self):
        if self.queue:
            out = self.queue.pop(0)
            print(out)
            return out
        else:
            self.isEmpty()

    def isEmpty(self):
        if not self.queue:
            print('Empty Queue')
    
    def peek(self):
        if self.queue:
            top = self.queue[-1]
            print(top)
            return top
        else:
            self.isEmpty()

q = queues()
q.enqueu(4)
q.enqueu(9)
q.enqueu(1)
q.peek()
