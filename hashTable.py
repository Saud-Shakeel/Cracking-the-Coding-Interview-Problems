class Node:

    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None

class hashTable:
    def __init__(self,size):
        self.size = size
        self.arr = [None]*size

    def hash_modulo(self, key):
        h_key = hash(key)
        mod = h_key% len(self.arr)
        return mod
    
    def set(self, key,val):
        mod = self.hash_modulo(key)

        if self.arr[mod] == None:
            self.arr[mod] = Node(key,val)
        else:
            current = self.arr[mod]
            while current.next:
                current = current.next
            current.next = Node(key,val)

    def get(self,key):
        mod = self.hash_modulo(key)
        current = self.arr[mod]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return None
        
    
h = hashTable(10)
h.set('abc',12)
print(h.get('abc'))