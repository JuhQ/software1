names = []

name = input("Give name, empty line exits: ")
while name != "":
  print(len(names))
  print(names)
  names.append(name)
  print(names)
  print(len(names))

  name = input("Give name, empty line exits: ")

print(names)

names.remove("Juha")

print(names)
