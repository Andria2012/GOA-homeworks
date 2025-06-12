month = int(input("შეიყვანე თვის ნომერი (1-12): "))

if month in [12, 1, 2]:
    print("სეზონი: ზამთარი")
elif month in [3, 4, 5]:
    print("სეზონი: გაზაფხული")
elif month in [6, 7, 8]:
    print("სეზონი: ზაფხული")
elif month in [9, 10, 11]:
    print("სეზონი: შემოდგომა")
else:
    print("არასწორი თვის ნომერია")








number = float(input("შეიყვანე რიცხვი: "))

if number > 0:
    print("რიცხვი დადებითია")
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნულია")









x = 5

if x > 10:
    print("მეტია 10-ზე")
elif x == 10:
    print("ზუსტად 10")
else:
    print("ნაკლებია 10-ზე")







age = int(input("შეიყვანე ასაკი: "))
income = int(input("შეიყვანე შემოსავალი: "))

if age < 18 or income < 10000:
    print("გათავისუფლებული ხარ გადასახადისგან")
else:
    print("გადასახადი გადასახდელია")




