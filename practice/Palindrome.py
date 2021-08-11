num = int(input("enter an number : "))
temp = num
revese = 0

while(num>0):
    dig = num*10
    revese = revese*10 + dig
    num / 10

if temp == revese:
    print("it is palindrome number")
else:
    print("it is not palindrome number")