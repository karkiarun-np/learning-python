# Check Palindrome Number
num = int(input("Enter a number: "))
temp = num
rev = 0
while num>0:
    dig = num%10
    rev = rev *10 + dig
    num = num//10

if rev == temp:
    print(temp, " Number is a Palindrome.")
else:
    print(temp, " Number is not a Palindrome.")