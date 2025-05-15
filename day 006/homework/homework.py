#Sequence: იგივეა რაც კოდის მაღლიდან დაბლა წაკითხვა.

#iteration: იგივეა რაც მოქმედების გამეორება.

#selection: საშუალებას გვაძლევს რომ პროგრამამ შეასრულოს სხვადასხა კოდზე დამოკიდული პირობა.




# ალგორითმი იგივეა რაც მოქმედების ეტაბობრივი მიმდრევრობა რომელიც კონკრეტული ამოცანების გაჭრის საშუალებას გვაძლევს.




print(True or False and False or True and False or False and False or False and True and False or True)
print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)
#ორივეში გამოვიტანთ TRUE-ს





number = int(input("შეიყვანეთ რიცხვი: "))

if (number % 2 == 0 and number >= 10) or number == 7:
    print(True)
else:
    print(False)





gela = "hello"

dima = str(9.50)

mogeli = str(True)

print(gela,dima,mogeli)


nugzari = 78

duduki = int("602")

doli = int(5.56)

print(nugzari,duduki,doli)




yukimia = 9.89

isagi = 9.32 + 4.90

kunigami = 5.08 // 2

print(yukimia,isagi,kunigami)




lorenzo = True

kaiser = False

snuffy = True and False

print(lorenzo,kaiser,snuffy)



year = int(input("შეიყვანეთ წელი: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is leap year")
else:
    print("This is not leap year")
