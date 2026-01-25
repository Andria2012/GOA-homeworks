s = set()
s.add(1)
s.add(2)
print(s)

a = {3, 4}
a.add(5)
print(a)

s = set()
for i in range(4):
    s.add(i)
print(s)

numbers = {1, 2, 3}
numbers.add(10)
print(numbers)

s = set()
for i in range(2, 9):
    if i % 2 != 0:
        s.add(i)
print(s)

colors = {"red", "blue"}
colors.add("yellow")
colors.add("green")
print(colors)

set1 = set()
set2 = set()

set1.add(1)
set1.add(2)

set2.add(2)
set2.add(3)

result = set1.union(set2)
print(result)