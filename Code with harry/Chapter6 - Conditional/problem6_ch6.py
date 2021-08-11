# write the program to calculate the grade by their grading system 
# 90-100 = excellent, 80-90 = A, 70-80 = B, 60-70 = C

a = int(input("Enter the marks obtained in exam :  "))

if(a>90 and a<=100):
    grade = "excellent"
elif(a>70 and a<90):
    grade  = "A"
elif(a>60 and a<70):
    grade = "B"
elif(a>50 and a<60):
    grade = "c"
else:
    grade = "oops you are fail"
print("your grade is ", grade)