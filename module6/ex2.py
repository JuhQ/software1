
number = input("Enter a number: ")

numbers = []


while number != "":
  num = float(number)
  numbers.append(num)
  number = input("Enter a number: ")

# numbers.sort()
# numbers.reverse()
numbers.sort(reverse=True)

print("The greatest numbers in descending order:")


for n in numbers[:5]:
  print(n)
