num = int(input('Enter a Number: '))
i=2
def isPrime(n):
   while(i*i<=n):
      if(n%i==0):
         return (f"{n} is not a Prime Number")
      return (f"{n} is a Prime Number")
      
print(isPrime(num))