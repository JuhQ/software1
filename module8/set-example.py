
games = {"Chess", "Puzzle", "Monopoly", "Diablo", "Puzzle"}
print(games)

games.add("Cluedo")

print(games)

for i in range(600):
  games.add("Cluedo")


print(games)

empty_set = set()
print(empty_set)

empty_set.add("New value")
print(empty_set)

print()

for game in games:
  print(game)

print()

for game in games:
  print(game)

print()

games.add("Carcassone")

for game in games:
  print(game)

print()

for game in games:
  print(game)

print(games)
games.remove("Diablo")
print(games)

print()

for game in games:
  print(game)

if "Diablo" in games:
  print("Diablo found in games set")

if "Cluedo" in games:
  print("Cluedo found in games set")
