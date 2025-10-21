#პირობითი ოპერატორები (Conditional operators) გამოიყენება პროგრამაში გადაწყვეტილების მისაღებად — ანუ იმისათვის, რომ კოდი იმუშავოს მხოლოდ მაშინ, როცა გარკვეული პირობა სრულდება.

age = 18
if age >= 18:
    print("სრულწლოვანი ხარ")
else:
    print("არასრულწლოვანი ხარ")

#ლოგიკური ოპერატორები გამოიყენება რამდენიმე პირობის კომბინაციისთვის.

num = 8

if num > 0 and num % 2 == 0:
    print("რიცხვი დადებითი და ლუწია")
else:
    print("პირობა არ შესრულდა")

x = 5

if x < 10 or x == 0:
    print("პატარა ან ნულია")
else:
    print("არ აკმაყოფილებს")

True and False or True or False and False and True or False and False
((True and False) or True or (False and False and True) or (False and False))
 
