# def Div_by_zero(func):
#   def inner(x,y):
#     if y ==0:
#       return "Quantity is zero"
#     return func(x,y)
#   return inner      
# @Div_by_zero
# def Unitprice (Amount,Quantity):
#   return Amount / Quantity

# # Main Program
# print (Unitprice(500,0))



def decorate(fun):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return inner



@decorate
def division(a,b):
    return a/b
print(division(2,4))