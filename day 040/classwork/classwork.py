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