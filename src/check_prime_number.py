# Check Prime Number
n = int(input("Enter a number to check Prime Number : "))
if n <= 1 :
    print("Number is Not a Prime Number.")
else:
    for i in range (2,n):
        if (n % i == 0):
            print("Number is not a Prime Number.")
            break
    else:
        print("Number is Prime Number.")
