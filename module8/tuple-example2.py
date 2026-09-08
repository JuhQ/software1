
days_of_the_week = ()

print(days_of_the_week)
print(len(days_of_the_week))
print(days_of_the_week)

# tuple index same as list
#                      0          1           2
days_of_the_week = ("Monday", 'Tuesday', "Wednesday", "Thursday", "Friday")

print(days_of_the_week[0:1])
print(days_of_the_week[1:])

fruits = "Orange", "Banana", "Apple"
print(fruits)
print(fruits[0:1])
print(fruits[1:])


values1 = 1, 2, 3, 4
values2 = 1, (2, 3), 4
values3 = (1, 2, 3, 4)
values4 = (1, (2, 3), 4)

print(values1)
print(values2)
print(values3)
print(values4)

# index    0    1     2   3 [0, 1, 2 (0, 1, [1])]  4       5
values5 = (1, (2, 3), 4,    [1,3,(4, 12, [2])],     True, "Strings")
print(values5)

print(values5[1])
print(values5[2])
print(values5[3])
print(values5[3][2])
print(values5[3][2][2])
print(values5[3][2][2][0])

menu = values5[3]
print(menu)
wed_menu = menu[2]

print(wed_menu)
print(wed_menu[2])
print(wed_menu[2][0])

print("before appending")
print(wed_menu[2])
print(values5)

wed_menu[2].append(1234)

print("after appending")
print(wed_menu[2])

print(wed_menu)
print(values5)

print(menu)

menu.append((1,2,3,"tuple"))
print(values5)

values5.append("no append for tuple")
