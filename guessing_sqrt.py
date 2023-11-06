def sqrt(n):
    u,l = n,1    
    while(u>=l):        
        mid = (u+l)//2
        square = mid*mid

        if square==n:
            return mid
        elif square>n:
            print('Too High')
            u = mid-1            
        else:
            print('Too Low')
            l = mid+1
            
    return -1

print(sqrt(5))

