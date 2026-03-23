# Uses of String Function
print("**************Uses of String Function******************")
while True:
    print("""Press 1 to Reverse the String
    Press 2 to count the String Characters
    Press 3 to check the Palindrome String 
    Press 4 to find the position of character in a string
    Press 5 to find the text type""")

    choice = int(input("Enter the selection : "))

    if choice == 1:
        sen = input("Enter the word or sentence to reverse : ")
        print(sen[::-1])
    elif choice == 2:
        sen = input("Enter the word or sentence to count characters : ")
        print("Total number of characters are : ", len(sen))
    elif choice == 3:
        sen = input("Enter the word to check Palindrome : ")
        rev = sen[::-1]
        if (sen == rev):
            print("It's Palindrome")
        else:
            print("It's not Palindrome")
    elif choice == 4:
        sen = input("Enter the word or sentence : ")
        f = input("Enter the character to find the position : ")
        print("Position of ", f, "is :", sen.index(f))
    elif choice == 5:
        sen = input("Enter any word : ")
        result = [""]
        if (sen.isalnum() == True):
            result.append("Alpha Numeric")
        if (sen.isalpha() == True):
            result.append("Alphabet")
        if (sen.isdecimal() == True):
            result.append("Decimal")
        if (sen.isdigit() == True):
            result.append("Digit")
        if (sen.isnumeric() == True):
            result.append("Numeric")
        if (sen.islower() == True):
            result.append("Lower Case")
        if (sen.isupper() == True):
            result.append("Upper Case")
        if (sen.istitle() == True): result.append("Title Case")
        print("Your string is : ", result)
    else:
        print("Wrong Choice")
    choice = input("Do you want to try again ? (y/n) : ")
    if choice == "n":
        break
print("Thank You")

