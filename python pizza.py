# input for pizza orders
print("welcome to python pizza deliveries.!")
size = input("what size of pizza do you want? S,M L?")
add_pepperoni = input("do you want peperroni?")
extra_cheese = input("do you want extra cheese?")

#program for pizza order
bill = 0

if size == "S":
    bill += 15
elif size =="M":
    bill += 20
elif size =="L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")