cars = [
    # First car (dictionary)
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2018
    },
    # Second car (dictionary)
    {
        "make": "Ford",
        "model": "Focus",
        "year": 2020
    },
    # Third car (dictionary)
    {
        "make": "VW",
        "model": "ID.3",
        "year": 2023
    }
]

index = 0
car_found = False
car_index = 0
for car in cars:
  print(car)

  if car['year'] == 2023:
    print("Car with year 2023 found")
    car_found = True
    car_index = index

  index = index + 1

if car_found:
  print(cars[car_index])
  print(cars[car_index]['make'])
  print(cars[car_index]['model'])


names = ['juha','ava']

print("index of car")

print(cars.index({"make": "VW", "model": "ID.3", "year": 2023}))
