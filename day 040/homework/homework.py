t = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5, 0)

positive = 0
negative = 0
zero = 0

for x in t:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

print("დადებითი:", positive)
print("უარყოფითი:", negative)
print("ნულები:", zero)


odd = []
even = []

for x in t:
    if isinstance(x, int): 
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

print("კენტი:", odd)
print("ლუწი:", even)


has_duplicates = len(t) != len(set(t))
print("მეორდება ელემენტები?:", has_duplicates)

max_num = t[0]
min_num = t[0]

for x in t:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x

print("უდიდესი:", max_num)
print("უმცირესი:", min_num)


sum_first_last = t[0] + t[-1]
print("პირველი + ბოლო:", sum_first_last)

product = 1
for x in t:
    product *= x

print("ყველა რიცხვის ნამრავლი:", product)


reversed_t = t[::-1]
print("შებრუნებული tuple:", reversed_t)


unique = tuple(set(t))
print("განმეორებების გარეშე:", unique)