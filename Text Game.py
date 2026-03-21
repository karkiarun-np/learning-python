#Game using text function
print("************TEXT FUNCTION GAME**************")
sentence=input("Enter a sentence : ")
while True:
    choice=int(input("""-----Enter a choice-----
    1. To convert sentence into uppercase
    2. To convert sentence into lowercase
    3. To count the number of characters in sentence
    4. To convert into Title Case Sentence
    Choice : """))
    if choice==1:
        print(sentence.upper())
    elif choice==2:
        print (sentence.lower())
    elif choice==3:
        print(len(sentence),"Characters")
    elif choice==4:
        print(sentence.title())
    else:
        print("Wrong Input")
    checkstep=input("Do you want to continue ? (y/n)")
    if checkstep=="n":
        break