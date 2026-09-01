#           0        1        2       3       4
names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

# hardcoded list of five items

# memory address 500 stores list
# names[0] address = 500 + 0
# names[1] address = 500 + 1
# names[2] address = 500 + 2


empty_list = []
print(empty_list)

print(names)

print(names[0])
print(names[1])

print(len(names))
print(len([]))

print(names[4])
print(names[-1])
print(names[len(names) - 1])


print(names[0:3])
print(names[0:2+1])

print(names[0:5])
print(names[0:6])

print(names[1:-1])

print(names)
print(names[2:])
print(names[3:])
print(names[4:])
print()
print(names[:2])
print(names[:1])
print(names[:3])
print(names[:4])


print()
print(names)

print(names[0])
names.reverse()
print(names[0])

print(names)



"""
len = get length of list
len()

length
lenght

lentgh

"""

if len(names) > 5:
  print("we have more than five items")
  print(names[5])
  print("this is after printing item at index 5")


if len(names) > 4:
  print(names[4])


