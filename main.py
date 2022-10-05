#ask input from the user
weight = float(input("Please input your weight(kg): " ))
height = float(input("Please input your height(cm): "))

#defining a function for BMI
height /= 100
bmi = weight / height**2
bmi = round(bmi, 1)

#print out the result and weight status by using if-elif-else statement
print(f"Your BMI is : {bmi}")

if bmi <= 18.5:
    print("Weight Status: Underweight")
elif bmi <= 24.9:
     print("Weight Status: Healthy")
elif bmi <=29.9:
    print("Weight Status: Overweight")
else:
    print("Weight Status: Obesity")