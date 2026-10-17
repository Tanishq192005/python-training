fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)


print("-"*20, end="\n")

for x in "banana":
  print(x)

print("-"*20, end="\n")

for i, fruit in enumerate(fruits, start=3):
  print(i, fruit)

print("-"*20, end="\n")

# Pattern printing
n=5
for i in range(1,n+1):
  for j in range(1, i+1):
    print(j, end=" ")
  print()

print("-"*20, end="\n")

n=5
for i in range(n, 0, -1):
  for j in range(1, i+1):
    print(j, end=" ")
  print()