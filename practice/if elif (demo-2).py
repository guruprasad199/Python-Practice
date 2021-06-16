bill_amt = int(input("enter bill_amt:  "))

if bill_amt >= 5000:
    bill_amt = bill_amt - 500
elif bill_amt >=3000:
    bill_amt= bill_amt - 300
elif bill_amt >=2000:
    bill_amt = bill_amt - 200
elif bill_amt >= 1000:
    bill_amt = bill_amt -100
print("you finaal bill is : ", bill_amt)