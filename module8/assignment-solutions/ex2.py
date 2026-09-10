name = input("Name: ")

names = set()

while name != "":
    # if-in statement can be used to check if item exists in set
    if name in names:
        print("Existing name")
    else:
        print("New name")

    # set being unique data structure
    # we do not need to have this wrapped in if-statement
    names.add(name)

    # .add() method in set will only add new item if the item does not exist

    # infinite loop if name is not asked (input function call) again
    name = input("Name: ")

# finally iterate through all the items in set one by one
for name in names:
    print(name)
