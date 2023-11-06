number = int(input('Enter a Number: '))
temp =number
reverse = 0

while(number>0):

    current_number = number%10
    reverse = reverse*10 + current_number
    number =number//10

print(f"Original Number: {temp}\n")

if temp == reverse:
    print(f"{temp} is a Palindrome")
else:
    print(f"{temp} is not a Palindrome")

      
