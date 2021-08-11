# write a code to check given  number is prime or not

num = int(input("Enter a number to check : "))
prime = True
for a in range(2, num):
    if (num % a == 0):
        prime = False
        break

if prime:
    print("number is prime")
else:
    print("number is not prime")


