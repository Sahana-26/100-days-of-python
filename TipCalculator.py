print("WElcome to tip calclator")
total_bill = float(input("enter the total bill amount"))
tip = float(input("what percentage of tip would u like to give? 10,15,20"))
people = int(input("how many people to split the bill?"))
split_amount = (((tip/100) * total_bill)+ total_bill) / people
print("Each person should pay: ",split_amount)