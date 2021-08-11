# write a python program to find some of natural number
def sumnumbers(num):
    if(num == 0):
        return num
    else:
        return sumnumbers(num-1) + num
        

number = int(input("Please Enter any Number: "))

total_value = sumnumbers(number)

print(total_value)