# key=value  key   value  key   value
numbers = {"Juha": "112", "Ava": "900", 0: "0 number"}

print(numbers)

print(numbers['Juha'])
print(numbers["Juha"])

# access values with the key
print(numbers["Ava"])

# key is case sensitive
# KeyError: 'ava'
# print(numbers["ava"])

if "ava" in numbers:
  print("Lowercase ava found")
  print(numbers["ava"])

if "Ava" in numbers:
  print("Uppercase Ava found")
  print(numbers["Ava"])

print(numbers[0])

print("\n\n")
for item in numbers:
  print(item)


# how to get key base on the value
# idea copied from https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
print(numbers.values())
print(list(numbers.values()))
print(list(numbers.values()).index("112"))
print(numbers.keys())
print(list(numbers.keys()))
print(list(numbers.keys())[list(numbers.values()).index("112")])

def get_key_by_value(dict, value):
  return list(dict.keys())[list(dict.values()).index(value)]

print(get_key_by_value(numbers, "112"))

