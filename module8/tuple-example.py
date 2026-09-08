# tuple index same as list
#                      0          1           2
days_of_the_week = ("Monday", 'Tuesday', "Wednesday")

print(days_of_the_week)

print(days_of_the_week[0])
print(days_of_the_week[len(days_of_the_week) - 1])
print(days_of_the_week[-1])

print(len(days_of_the_week))
print(len((1,2,3,4,5)))

print(days_of_the_week.count("Monday"))
print(days_of_the_week.index("Monday"))

# print(days_of_the_week[len(days_of_the_week)])

if len(days_of_the_week) > 10:
  print(days_of_the_week[10])
