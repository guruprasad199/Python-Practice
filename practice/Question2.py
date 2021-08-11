# Bank Account Class 1. Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance. 2. Create a constructor with parameters: accountNumber,name, balance. 3. Create a Deposit() method which manages the deposit actions. 4. Create a Withdrawal() method which manages withdrawals actions. 5. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account. 6. Create a display() method to display account details. 7. Give the complete code for the BankAccount class.





# BankAccount class
# class Bankaccount:

#         "bank acount details"

# 	def __init__(self, accountNumber,name, balance):
#         self.accountNumber=accountNumber
#         self.name=name
#         self.balance=balance

#     # Function to deposite amount
#     def deposit(self):
#             amount = float(input("Enter amount to be deposited: "))
#             self.balance += amount
#             print("\n Amount Deposited:", amount)

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank:
	def __init__(self):
                
        # self.charges=0
		self.balance=0
		print("Welcome to your bank account")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

    	def apply(self):
       		#  self.charges = 5
        	#  self.balance = self.balance*self.charges/100
			 self.balance = (95/100)*self.balance




    	def display(self):
	   		 print("\n Available Balance=",self.balance)

s = Bank()

s.deposit()
s.withdraw()
s.apply()
s.display()

