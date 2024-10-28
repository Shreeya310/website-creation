height=float(input("kindly enter your height in centimetres="))
weight=float(input("kindly enter your weight in kilograms="))

BMI=weight/(height/100)**2
print("your BMI is",BMI)
if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
else:
    print("you are severly obese")