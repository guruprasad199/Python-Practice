number_list = []
num = int(input("enter the number: "))
for i in range(0, num):
    print("enter the index of : " , i)
    item = int(input())
    number_list.append(item)
print("here is the list", number_list)