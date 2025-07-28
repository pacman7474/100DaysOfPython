#height = 1.65
#weight = 84
#
#bmi = weight / height ** 2
#
#print(round(bmi,2))

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?> ")
tip = input("How much tip would you like to give? 10, 12, 15> ")
tip_and_bill = float(total_bill.replace("$","")) * (1 + round(float(tip),2)/100)
num_people = input("How many people to split the bill?> ")
print(f"Each person should pay: ${round(tip_and_bill/int(num_people),2)}")