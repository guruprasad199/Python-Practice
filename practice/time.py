def bmi_script_4(age,height, weight):
     BMI = round(weight/ (height * height), 1)
     return "The BMI is", BMI

if __name__ == '__main__':
     age= int(input("Hi Argo, What is your Age?"))
    #  print(age)
     height = float(input("What is your Height in metres?"))
    #  print(height)
     weight = int(input("What is your Weight in Kg?"))
     print(weight)
     bmi_script_4(age,height, weight)
