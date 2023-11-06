class stacks:
    def __init__(self,size):
        self.size = size
        self.stack_size = self.size//3
        self.arr = [None] * self.size
        self.pointers = [0,self.stack_size, 2*self.stack_size]

    def push(self,val,stack_num):
        if self.pointers[stack_num] < (stack_num+1) * self.stack_size:            
            self.arr[self.pointers[stack_num]] = val
            self.pointers[stack_num] +=1            
        else:
            print(f"Stack Number {stack_num} is already full.")
            
            
    
    def pop(self,stack_num):
        if self.pointers[stack_num] > stack_num*self.stack_size:
            popped_val = self.arr[self.pointers[stack_num]-1]
            self.arr[self.pointers[stack_num] -1] = None
            self.pointers[stack_num] -=1
        else:
            return f"Stack Number {stack_num} is empty."
        return popped_val

s = stacks(8)
s.push(1,0)
s.push(2,0)
s.push(10,1)
s.push(8,2)
s.push(5,0)
s.push(33,1)

print(s.pop(0))
print(s.pop(0))
print(s.pop(1))
print(s.pop(2))
print(s.pop(2))
