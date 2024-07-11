# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆
bmi = weight / height**2

if bmi < 18.5 :
  print(f"Your BMI is {bmi}, you are underweight.")
#Write your code below this line 👇
elif bmi in range(18.5,25):
  print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi in range(25,30):
  print(f"Your BMI is {bmi}, you have slightly overweight.")
elif bmi in range(30,35):
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")