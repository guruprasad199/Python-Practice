# make a spam detector if the text match with your record make it spam and print the statement it is spam text

text = input("Enter the text :  ")

if("make a lot of money" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("text is spam")
else:
    print("text is not spam")
