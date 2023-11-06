def all_fib(n):

    memo = [0] * (n+1)
    for i in range(n+1):
        print(f"{i}: {fib(i,memo)}")

def fib(n, memo):
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif memo[n]>0:
        return memo[n]        
    else:
        memo[n] = fib(n-1,memo)+fib(n-2,memo)
    
    return memo[n]

print(all_fib(7))

