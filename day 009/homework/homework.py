num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი კენტია.")

num = int(input("შეიყვანეთ რიცხვი: "))

if num < 0:
    print("რიცხვი უარყოფითია.")
else:
    print("რიცხვი ნულის ტოლი ან მეტია.")

num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი კენტია.")

if num < 0:
    print("რიცხვი უარყოფითია.")
else:
    print("რიცხვი ნულის ტოლი ან მეტია.")

age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age < 18:
    print("დაბლოკილი ხარ.")
else:
    print("ზრდასრული ხარ.")

color = input("შეიყვანეთ ფერი (მწვანე, ყვითელი, წითელი): ").lower()

if color == "მწვანე":
    print("წადი.")
elif color == "ყვითელი":
    print("მოემზადე.")
else:
    print("გაჩერდი.")

price = 22.50
money = float(input("შეიყვანეთ რამდენი ფული გაქვთ: "))

if money >= price:
    change = money - price
    print("ხურდა:", change, "ლარი")
else:
    missing = price - money
    print("გაკლია:", missing, "ლარი")