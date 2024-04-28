a = int(input("enter the starting = "))
b = int(input("enter the ending number = "))
# c=int(input("enter the updation:"))
choice = int(input("0for forward &1 for reverse"))
choice2 = int(input(" 2 for horizontal& 3 for vertical"))
if (choice == 1):
    if (a > b):
        a, b = b, a

        temp = a
        a = b
        b = temp
        for i in range(a, b - 1, -1):
            if (choice2 == 2):
                print(i, end=',')
            else:
                print(i)


else:
    if (choice == 0):
        for i in range(a, b + 1, 1):
            if (choice2 == 2):
                print(i, end=',')
            else:
                print(i)