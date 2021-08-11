# while (1):
#     print("\nEnter a number less than 100 to find out square: ")
#     print("press 0 to exit: ")
#     num  = int(input())
#     if num == 0:
#         print("programs end thank you")
#         break
#     elif num > 100:
#         print("number i greater than 100. try again")
#         continue
#     print("\n Square of", num, "is ", num*num )


# num = (1,2,3, None ,4)
# print(len(num))

# import datetime

# start = datetime.datetime.strptime("2-08-2021", "%d-%m-%Y")
# end = datetime.datetime.strptime("07-08-2021", "%d-%m-%Y")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# for date in date_generated:
#     print (date.strftime("%d-%m-%Y"))

# import datetime;
# print( [(datetime.date.today() - datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(-5,0)])


import datetime;
# M = ([(datetime.date.today() - datetime.timedelta(days=x)).strftime('%d-%m-%Y') for x in range(-5, 0)])
# M.reverse()
# print(M)

from datetime import date

def dates():
    yield date.today()
    yield date.today()


values = dates()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)



    # print("Today's date:", today)

