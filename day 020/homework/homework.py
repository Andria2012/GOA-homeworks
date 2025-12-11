numbers = []

for i in range(3):
    num = input("შეიყვანეთ რიცხვი: ")
    numbers.append(num)

numbers.extend(["green", "yellow", "purple"])

print(numbers)

animals = ["cat", "dog", "lion", "tiger"]

size = len(animals)

print("სიის ზომაა:", size)


word = input("შეიყვანეთ სიტყვა: ")

length = len(word)

print("ამ სიტყვას აქვს", length, "სიმბოლო.")

text = "apple orange banana"

words = text.split()

print(words)

name = input("შეიყვანეთ თქვენი სახელი: ")

print("YOUR NAME IS:", name.upper())

TEXT = "PROGRAMMING IS FUN"

print(TEXT.lower())

words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print(sentence)

names = ["Ana", "Gio", "Saba"]

result = ", ".join(names)
print(result)

movie = input("შეიყვანეთ თქვენი საყვარელი ფილმის სახელი: ")

print(movie.capitalize())