def bmi_script_4(age,height, weight):
     BMI = round(weight/ (height * height), 1)
     return "THE BMI is" + str(BMI)
if __name__ == '__main__':
     age= int(input("Hi Argo, What is your Age?"))
     height = float(input("What is your Height in metres?"))
     weight = int(input("What is your Weight in Kg?"))
     bmi_script_4(age, height, weight)
     
     