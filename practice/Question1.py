# Rectangle Class 1. Write a Rectangle class, allowing you to build a rectangle with length and width attributes. 2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of  
#  the rectangle. 3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.



class Rectangle():
    ''' Rectangle class Program'''

    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length

    def calculate_area(self):
        return self.breadth*self.length

length=int(input("Enter length of rectangle: "))
breadth=int(input("Enter breadth of rectangle: "))
rec1=Rectangle(length,breadth)
print("Area of rectangle:",rec1.calculate_area())