choice=int(input("Enter number of row for a triangle pattern : "))
# For Triangle
for i in range(1,choice+2):
    for j in range(1,i):
        print(j,end=" ")
    print()
# For Reverse Triangle
for i in range(0,choice+2):
    for j in range(1, choice-i):
        print(j,end=" ")
    print()

