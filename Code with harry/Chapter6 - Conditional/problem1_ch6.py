# we have 4 user find the greatest number enterd by the user
a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
d = int(input("enter a number : "))
if(a>d):
    f1 = a
else:
    f1 = d

if(b>c):
    f2 = b
else:
    f2 = c

if(f1>f2):
    print(str(f1) + " is greatest")
else: 
    print(str(f2) + " is greatest")





