# Count the squr between two numbers 

num = int(input("Enter 1st number : "))
num1 = int(input("Enter 2nd number: "))
print("Perfect sqr between two number ", end=" ")

while num<=num1:
    for i in range(1, num):
        if i*i==num:
            print(num, end=" ")
    
    num=num+1
