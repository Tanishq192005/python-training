fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)


print("-"*20, end="\n")

for x in "banana":
  print(x)

print("-"*20, end="\n")

for i, fruit in enumerate(fruits, start=3):
  print(i, fruit)