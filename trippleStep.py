def trippleStep(n, memo):
    memo = [0] * (n+1) # initialize the list with zeros
  
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    
    if memo[n] == 0:
        memo[n] = trippleStep(n-3, memo) + trippleStep(n-2, memo) + trippleStep(n-1, memo)
    return memo[n]

print(trippleStep(7, []))
