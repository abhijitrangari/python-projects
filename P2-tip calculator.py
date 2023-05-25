# welcome screen of tip calculator
print("welcome to tip calculator!!!")
# 3 variables for bill,tip and people with input for the same 
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10 ,12 or 15? "))
people = int(input("how may people to split the bill? "))
# tip as percent calculation
tip_as_percent = tip / 100
# total tip amount formula
total_tip_amount = bill * tip_as_percent
# total bill amount
total_bill = bill + total_tip_amount
# bill per person formula
bill_per_person = total_bill / people
# final amount in round to 2 decimals
final_amount = round(bill_per_person,2)
# final amount each person has to pay
print(f"each person should pay ${final_amount}")







