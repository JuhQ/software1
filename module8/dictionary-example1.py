# key=value  key   value  key   value
# duplicate keys not allowed
# duplicate values allowed
numbers = {
  "Juha": "112",
  "Juha1": "112",
  "Juha": "500",
  "Juha": "600",
  "Ava": "900",
  "ava": "800",
  0: "0 number"
}

print(numbers)



numbers2 = {
  "Juha": ["500", "300"],
  "Juha": ["500", "300"],
  "Juha": ["500", "300"],
  "Juha2": {"books": ["book1", "book2"]},
  "Juha1": "112"
}

print(numbers2)
print(numbers2['Juha'][0])
print(numbers2['Juha'][1])

print(numbers2['Juha2']['books'])
print(numbers2['Juha2']['books'][1])




numbers2['new_key'] = 123
print(numbers2)
numbers2['new_key'] = 200
print(numbers2)
numbers2['new_key'] = 500
print(numbers2)

print(numbers2['new_key'])

juha = numbers2.pop("Juha")
print(numbers2)

print(juha)

print(numbers2)

numbers2["Juha2"] = "my new data"
print(numbers2)

empty_dict = {}


# for in with just the dict variable will get you keys
for number in numbers:
  print(number)

# if you need the values, use .values() method
for number in numbers.values():
  print(number)


if "Juha" in numbers:
  print("Juha found")

if "juha" in numbers:
  print("juha found")


