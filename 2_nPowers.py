num = int(input('Enter a Number: '))

def nPowers(n):
    if n<1:
        return 0
    elif n==1:
        return n
    else:
        prev= nPowers(n//2)
        print(f"previous: {prev}")
        curr= prev*2
        print(f"current: {curr}")
    return curr

print('Output:',nPowers(num)) 