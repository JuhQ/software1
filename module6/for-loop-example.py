names = ["Juha", "Ava"]

name = input("Enter the first name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

print(names)

#print(names[0])
#print(names[1])

i = 0
for name in names:
    print(f"Value at index {i} is {name}")
    i = i + 1

if "Ahmed" in names:
    print("Ahmed found in list")
