# in this assignment clicking on the check button in moodle will be helpful as it gives more hints on what to do

# this needs to be also inside the while
print("") # why does this assignment require empty line in the beginning - who made this stupid assignment (plot twist, it as I)

print("Airport Data Management")
print("1. Enter a new airport")
print("2. Fetch airport information")
print("3. Quit")

option = input("Please choose an option (1-3): ")

# empty dictionary to store airports
airports = {}

# comparing string 3, not number 3
while option != "3":
    if option == "1":
        # store info (what?) to dictionary
        # looking at input it seems we need to ask two times (2 x input calls)
        icao = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        # store the new airport to dictionary
        # dictionaries are key-value stores, icao variable here is the key
        airports[icao] = name

        print(f"Airport {name} with ICAO code {icao} has been added.")
    elif option == "2":
        # fetch information from dictionary
        icao = input("Enter the ICAO code: ")

        # get airport information from the dictionary and print it
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    print("")

    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    # in these kind of assignments / situations the while loop usually ends with input
    # the while condition "option != "3"" will check should we continue to next line
    option = input("Please choose an option (1-3): ")


print("Thank you for using the Airport Data Management system. Goodbye!")
