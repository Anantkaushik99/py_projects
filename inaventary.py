print('ENTRY BY SHOPKEEPER')
n=int(input('Enter number of items : '))
lst=[]
for i in range(0,n):
    a=input('Enter name of item : ')
    b=int(input('Enter quantity of '+a+' : '))
    r=int(input('Enter item rate : '))
    a=a.lower()
    l=[]
    l.append(a)
    l.append(b)
    l.append(r)
    lst.append(l)
print('ENTRY BY CUSTOMER')
n=int(input('Enter number of items : '))
bud=int(input('Enter budget : '))
b2=True
bill=0
for i in range(0,n):
    a=input('Enter name of item : ')
    b=int(input('Enter quantity of '+a+' : '))
    a=a.lower()
    flag=0
    for i in lst:
        if i[0]==a:
            flag+=1
            if b<=i[1]:
                i[1]-=b
                z=b*i[2]
                bill+=z
            else:
                print('Quantity not available')
                b2= False
                break
            break
    if flag==0:
        print('Item not available')
        b2= False
        break
if bud>=bill:
    if b2:
        print('Your order has been confirmed!!')
        print('Your total payable amount is',str(bill)+'.')
else:
    print('Sorry you dont have enough money')