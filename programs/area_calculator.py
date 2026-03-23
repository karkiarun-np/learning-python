# Area Calculator
print("**********Area Calculator**********")
while True:
    print("""
    Press 1 to calculate area of a square
    Press 2 to calculate area of a rectangle
    Press 3 to calculate area of a circle
    Press 4 to calculate area of a triangle """)

    choice = int(input("Enter your choice 1- 4 : "))

    if choice == 1:
        while True:
            side = int(input("Enter the side length of the square : "))
            if side > 0:
                area = side * side
                print("The area of the square is: ", area)
            else:
                print("Wrong Input")
            check = str(input("Do you want to calculate area of another square ? (y/n) : "))
            if (check == "n"):
                break
    elif choice == 2:
        while True:
            l = int(input("Enter the length of the rectangle : "))
            b = int(input("Enter the breadth of the rectangle : "))
            if (l > 0 and b > 0):
                area = l * b
                print("The area of the rectangle is: ", area)
            else:
                print("Wrong Input")
            check = input("Do you want to calculate area of another rectangle ? (y/n) : ")
            if check == "n":
                break
    elif choice == 3:
        while True:
            r = int(input("Enter the radius of the circle : "))
            if (r > 0):
                area = (22/7) * r *r
                print("The area of the circle is: ", area)
            else:
                print("Wrong Input")
            check = input("Do you want to calculate area of another circle ? (y/n) : ")
            if check == "n":
                break
    elif choice == 4:
        while True:
            base = int(input("Enter the base of the triangle : "))
            height = int(input("Enter the height of the triangle : "))
            if (base > 0 and height > 0):
                area = 0.5 * base * height
                print("The area of the triangle is: ", area)
            else:
                print("Wrong Input")
            check = input("Do you want to calculate area of another triangle ? (y/n) : ")
            if check == "n":
                break
    else :
        print("Invalid Choice")
    check = input("Do you want to repeat the calculator ? (y/n) : ")
    if check == "n":
        break
