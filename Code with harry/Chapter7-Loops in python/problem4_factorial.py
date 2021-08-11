# write a code to calculate factorial of the given number enter by user
factorial = 1
num = int(input("Enter the number : "))
for a in range(1, num+1):
    factorial = factorial*a
print(f"the factorial of {num} is {factorial}")