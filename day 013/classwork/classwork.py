a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))
c = int(input("შეიყვანეთ მესამე რიცხვი: "))
print("სამი რიცხვის ჯამი არის:", a + b + c)






print("nრიცხვები 10-დან 1-მდე:")
for i in range(10, 0, -1):
    print(i)






print("nკენტი რიცხვები 1-დან 100-მდე:")
for i in range(1, 101):
    if i % 2 == 1:
        print(i)









print("nრიცხვები რომლებიც 3-ზე უნაშთოდ იყოფა:")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)











x = int(input("შეიყვანე რიცხვი x: "))
i = 1
while i <= x:
    print(i)
    i += 1





x = int(input("შეიყვანე რიცხვი x: "))
i = 1
while i <= x:
    print(i)
    i += 1





i = 2
while i < 100:
    print(i)
    i += 2









i = 1
count = 0
while i <= 50:
    if i % 2 == 0:
        count += 1
    i += 1
print("ლუწი რიცხვების რაოდენობაა:", count)










i = 0
while i <= 100:
    print(i)
    i += 10