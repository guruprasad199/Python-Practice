# Book Class
# Define a Book class with the following attributes: Title, Author (Full name), Price. 1. Define a constructor used to initialize the attributes of the method with values entered by the user. 2. Set the View() method to display information for the current book. 3. Write a program to testing the Book class.



class Book():
    

    def __init__(self, title, Author, Price):
        self.title=title
        # self.Author=Author
        # self.Price=Price
        
    def Title(self):
        price = int(input("Enter the price of book : "))
        return price

re1 = Book(Title)
print("\n title is : ", re1.Title())

    # def Name(self):
    #     Name = input("Enter the book name : ")
    #     return Name

    # def View(self):
    #     Book()
    #     print("\n Detais of book name : ", Book.Name())
    #     print("\n price of book  ", Book.Price())
    #     Book.View()
        
# s = Book

# s.Price()
# s.Name()
# s.View()