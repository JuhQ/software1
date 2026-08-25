money = float(input("Give money: "))

cost_of_coffee = 5


if cost_of_coffee <= money:
  print("You can buy coffee")

if money >= cost_of_coffee:
  print("You can buy coffee")

  if money >= 20:
    print("You can also buy cake")

  takeout = input("Coffee to go? ")

  if "yes" == takeout:
    print("User is taking the coffee to go")

  if takeout == "yes":
    print("User is taking the coffee to go")

  if takeout == "no":
    print("User is having the coffee in the cafe")
