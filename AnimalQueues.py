class animalQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.count = 0
    
    def enqueue(self,animal):
        self.count +=1
        if str.lower(animal) == 'cat':
            self.queue1.append((animal,self.count))
        else:
            self.queue2.append((animal,self.count))
    
    def catDequeue(self):
        if not self.queue1:
            return 'Empty Cat Queue'
        return self.queue1.pop(0)
    
    def dogDequeue(self):
        if not self.queue2:
            return 'Empty Dog Queue'
        return self.queue2.pop(0)
    
    def anyDequeue(self):
        if not self.queue1 and not self.queue2:
            return 'Empty Cat and Dog Queues'
        if self.queue1:
            if self.queue1[0][1] > self.queue2[0][1]:
                return self.queue2.pop(0)
        elif not self.queue1:
            return self.queue2.pop(0)
        elif not self.queue2:
            return self.queue1.pop(0)
        return self.queue1.pop(0)

q = animalQueues()
q.enqueue('cat')
q.enqueue('dog')
q.enqueue('cat')
q.enqueue('dog')
q.enqueue('cat')
print(q.catDequeue())
print(q.catDequeue())
print(q.catDequeue())
print(q.dogDequeue())
print(q.anyDequeue())
print(q.anyDequeue())
