def sumofDigits(n):
    sum=0
    while(n>0):
        sum = sum + (n%10)
        n = n//10
    return sum

print(sumofDigits(592))