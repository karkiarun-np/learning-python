# Fibonacci Series
a=0
b=1
n=int(input("Enter the number for Fibonacci Series : "))
if (n==1):
    print(n)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c = a+b
        a = b
        b = c
        print(c)

