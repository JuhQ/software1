# fn is short function

import random

def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first, second

def cast2():
    (first, second) = (random.randint(1,6), random.randint(1,6))
    return (first, second)

value = cast()
#print(value)

print(cast())
print(cast2())

die1, die2 = value
#print(f"The dice show {die1} and {die2}.")
