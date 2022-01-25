# 🚨 Enjoy Pizza👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size=="SMALL":
  bill += 15
elif size=="MEDIUM":
  bill += 20
else :
  bill += 25
if add_pepperoni== "Y":
  if size=="SMALL":
    bill+=2
  else:
    bill+=3
if extra_cheese=="Y":
  bill+=1
print(f"your bill for {size} pizza is {bill}")
  










