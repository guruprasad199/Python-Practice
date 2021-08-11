# age = 45

# if(age>34 or age<56):
#     print("you can work with us")
# else:
#     print("sorry u can't work with us")






# age = 45

# if(age>34 and age<56):
#     print("you can work with us")
# else:
#     print("sorry u can't work with us")

def sm(lists):
    min = lists[0]
    for a in lists:
        if a > min:
            min = a
    return min
print(sm([4,5,7,8,3,2,4]))