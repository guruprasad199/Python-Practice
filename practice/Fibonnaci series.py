# def reur_fibo(num):
#     if num <= 1:
#         return num
#     else:
#         return (reur_fibo(num-1) + reur_fibo(num-2))
# nterms = int(input("enter number or element : "))
# if nterms <= 0:
#     print("please enter positive ingeger")
# else:
#     print("fibonacci sequence: ")
#     for i in range(nterms):
#         print(reur_fibo(i))



def fibo(num):
    if num<=1:
        return num
    else:
        return (fibo(num-1) + fibo(num-2))
taketerm = int(input("enter number: "))
print("fibonacci series")
for i in range(taketerm):
    print(fibo(i))
