a = []
n = int(input("enter number of element: "))
for i in range(1, n+1):
    b = int(input("enter element: "))
    a.append(b)
a.sort()
print("Largest element is: ", a[n-1])

print(" _______________________________________________________")
u = []
d = int(input("enter number: "))
for o in range(1, d+1):
    print(o)
    z = int(input("try : "))
    u.append(z)
    print(u)
u.sort()
print(u)
