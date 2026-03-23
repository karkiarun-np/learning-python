row_no=int(input("Enter number of row for a triangle pattern : "))

# For Triangle
print("""
******Triangle Pattern******""")
for i in range(1,row_no+2):
    for j in range(1,i):
        print(j,end=" ")
    print()

# For Reverse Triangle
print("""

******Reverse Triangle Pattern******""")
for i in range(0,row_no+2):
    for j in range(1, row_no-i):
        print(j,end=" ")
    print()

