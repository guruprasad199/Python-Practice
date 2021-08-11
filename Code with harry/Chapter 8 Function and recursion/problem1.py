# find the gretest number from the three int value

def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1

    else:
        if(num2>num3):
            return num2
        else:
            return num3
            
              

m = maximum(3,88,7)
print("the maximum number is " + str(m))
    