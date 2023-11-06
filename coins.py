def coins(n):
    a, b, c, d = 0, 0, 0, 0

    if n == 1: return 1
    if n == 5: return 1  
    if n == 10: return 1  
      
    
    if n >= 25:
        a = coins(n - 25)
        
    if n >= 10:
        b = coins(n - 10)        
    
    if n >= 5:
        c = coins(n - 5)        
    
    if n >= 1:
        d = coins(n - 1)       
    
    return a+ b+ c+ d 

print(coins(12))

