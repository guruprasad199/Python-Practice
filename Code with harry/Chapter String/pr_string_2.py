# write a program to fill letter templete given below with name and date

letter = '''  Dear <|NAME|> , 
Happy to inform you that you are selected in Infosys 
Great day ahead 

Thanks and regards 
Billo

<DATE> '''


name = input("Enter a name: ")
date = input("Enter date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<DATE>", date)
print(letter)
