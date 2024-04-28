print("Welcome To Vote")

age = int(input("Enter Your age :- "))
if age >=18:
    print("You are eligible to vote..")
    print("1 for 'BJP'\n2 for 'AAP'\n3 for 'BSP'\n4 for 'CPI(M)'\n5 for 'INC'\n6 for 'NPP' : ")

    choice = int(input("Enter your voting number : "))
    if choice == 1:
        print("Your Vote For BJP")
    elif choice == 2:
        print("Your Vote For AAP")
    elif choice == 3:
        print("Your Vote For BSP")
    elif choice == 4:
        print("Your Vote For INC")
    elif choice == 5:
        print("Your Vote For NPP")
    else:
        print("invalid Choice: ")

else:
    print("You are note eligible to vote")