# write a code to check the number is even or odd by using for loop

num = int(input("Enter  the number to check :  "))
Even = False
for a in range(1, num):
    if (num%2==0):
        Even = True
        break

if  Even:
    print("The number is even")
else:
    print("the number is odd")

