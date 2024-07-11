print("Welcome to the tip calculator!")
total_bill = float(input("Please enter the total bill :Rs."))
tip_in_percentage = int(input("Please enter how much tip you want to give 10%,12%,15% :")[1])
total_tip = total_bill + total_bill * tip_in_percentage/100
contri_per_person = int(input("Please enter the the number of persons to split the bill :"))
Total_contri_per_person = (total_bill + tip_in_percentage )/contri_per_person
print(f"Each person should pay {Total_contri_per_person} rupees")