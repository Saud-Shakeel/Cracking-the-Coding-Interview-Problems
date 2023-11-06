class arrayList:

    def __init__(self):
        self.length = 1
        self.current = -1
        self.arr = [None]*self.length

    def set(self, val):
        if self.current < self.length-1:
           self.arr[self.current+1]=val
           self.current +=1
        else:
           temp = [None] * self.length*2
           for i in range(self.length):
               temp[i]=self.arr[i]
               
           self.arr = temp   
           self.length *= 2             
           self.arr[self.current+1]=val
           self.current+=1
        print(self.arr)

    def get(self,val):
        arr = self.arr[self.current]
        return arr

         
    
a= arrayList()
a.set(1)
a.set(10)
a.set(5)
a.set(10)
a.set(1)
a.set(1)

    



