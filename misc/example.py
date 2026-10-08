
import time
string = "hello world" * 1000

for char in string:
    print(char, end='', flush=True)
    time.sleep(.05)

print()

print(int(" 10"))
print(" 10")


bag = [
  {"name": "banana", "price": 5},
  {"name": "apple", "price": 5},
]

i = 0
found = None
for item in bag:
  #print(item)

  if item["name"] == "apple":
    print("found apple")
    found = i

  i += 1

if found:
  print(bag[found]["name"])


print("sleeping for five hours")

time.sleep(1)
print("slept for 1 hour")
time.sleep(1)
print("slept for 2 hour")
time.sleep(1)
print("you are now rested")



print("https://en.wikipedia.org/wiki/Bit_numbering")
