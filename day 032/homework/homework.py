my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)
my_set = {1, 2, 3}
my_set.discard(5)

my_set = {1, 2, 3}
my_set.remove(2)


my_set = {1, 2}
my_set.update([3, 4, 5])
print(my_set)

my_set = {1, 2}
my_set.add(3)

my_set = {1}
my_set.update([2, 3, 4])

Copy code
my_set = {1, 2, 3}
my_set.remove(2)

my_set = {1, 2, 3}
my_set.discard(2)

my_set = set()

for i in range(1, 21):
    my_set.add(i)
print(my_set)

my_set = set()

for i in range(1, 21):
    my_set.update([i])
print(my_set)

my_set = set()
i = 1

while i <= 20:
    my_set.add(i)
    i += 1
print(my_set)

my_set = set()
i = 1

while i <= 20:
    my_set.update([i])
    i += 1
print(my_set)

my_set = set(range(1, 21))
i = 1

while i <= 20:
    if i % 2 == 0:
        my_set.discard(i)
    i += 1

print(my_set)