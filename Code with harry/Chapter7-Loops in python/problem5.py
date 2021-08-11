# write a code to find out sum of n natural number using while loop

# n = int(input("Enter the number : "))


# sum = 0 

# while sum>n:
#     sum = sum + 1
# print(sum)

num = int(input("Enter a number: "))  
  
# if num < 0:  
#    print("Enter a positive number")  
# else:  
sum = 0  
   # use while loop to iterate un till zero  
while(num > 0):  
    sum += num  
    num -= 1  
print("The sum is",sum)  