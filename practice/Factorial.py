def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
num = int(input("Enter number to calculate factorial :  "))
if num == 0:
    print("factorial of 1 is 1")
if num < 0:
    print("can not find the factorial for negative number")

print("factorial of ", num , "is: ", factorial(num))


