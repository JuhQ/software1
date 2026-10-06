import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"asd.json")
path1 = os.path.join(os.path.dirname(__file__), "..","asd.json")
path2 = os.path.join(__file__, "..", "..", "asd.json")

print(path)
print(path1)
print(path2)

print()

print(os.path.abspath(path))
print(os.path.abspath(path1))
print(os.path.abspath(path2))
