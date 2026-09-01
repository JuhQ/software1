names = []

print(names)
names.append("Juha")
print(names)
names.append("Ava")
print(names)
names.append("Matti")
print(names)

matti_index = 2

print(names[matti_index])
print(names.index("Matti"))

names.remove("Juha")
print(names)
#print(names[matti_index])


#names.insert(1, "Timo 1")
names.insert(100, "Timo 100")
names.insert(-1, "Timo -1")
#names.insert(-1, ["Timo -1"])
print(names)
# this no longer prints Matti, which the dev expected
print(names[matti_index])



print(names)

names.extend(["Vito", "Veikko", "Cool cats"])

print(names)

another_list_of_names = ["Coffee", "Puzzle"]

names.extend(another_list_of_names)
print(names)

print(names.index("Matti"))

names.append("Matti")
names.append("Matti")
names.append("Matti")

print(names)
print(names.index("Matti"))


if "Ava" in names:
  print("Ava found in names list")

if "ava" in names:
  print("ava found in names list")

if "Juha" in names:
  print("Juha found in names list")
else:
  print("Juha not found")


print(names)

names.sort()

print(names)

print(names)

names.reverse()

print(names)


print("Break until 14.25")
