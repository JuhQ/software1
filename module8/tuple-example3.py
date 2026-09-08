days_of_the_week = ("Monday", 'Tuesday', "Wednesday", "Thursday", "Friday")

first = days_of_the_week[0]

print(days_of_the_week)
print(first)

first = "Saturday"

print(days_of_the_week)
print(first)

# TypeError: 'tuple' object does not support item assignment
# days_of_the_week[0] = "Saturday"
print(days_of_the_week)

for day in days_of_the_week:
  print(day)

if "Monday" in days_of_the_week:
  print("Monday found")
