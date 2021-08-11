string = "Hellow How Are You My Friend"

def swap_case(string):
    output = ' '
    for char in string:
        if(char.isupper() == True):
           output = output + (char.lower())
        if(char.islower()==True):
            output = output + (char.upper())
        else:
            output = output + char
    return output

ok = swap_case(string)
print(ok)




