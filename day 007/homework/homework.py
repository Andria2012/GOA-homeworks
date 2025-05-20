i = 1
while i <= 10:
    print(i)
    i += 1




i = 10
while i >= 1:
    print(i)
    i -= 1









# A "while loop" in programming is a control flow statement that repeatedly executes a block of code as long as a given condition is true. It continues to loop until the condition becomes false, at which point the loop terminates. This is useful when you don't know in advance how many times a specific code section needs to be run. 




password = "python123"

user_password = input("enter your password:  ")

while user_password != password:
    user_password = input("enter you password again: ")

print("welcome")





n = int(input("შეიყვანე რიცხვი n: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("ჯამი არის:", sum)