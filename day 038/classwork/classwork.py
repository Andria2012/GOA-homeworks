person = {
    "name": "Nika",
    "surname": "Beridze",
    "age": 20,
    "city": "Tbilisi"
}

print("Keys:")
for key in person:
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

del person["city"]
print("\nAfter deleting 'city':")
print(person)

person.pop("surname")
print("\nAfter pop 'surname':")
print(person)

person.clear()
print("\nAfter clear():")
print(person)

person = {
    "name": "Nika",
    "surname": "Beridze",
    "age": 20,
    "city": "Tbilisi"
}

person["age"] = 25
print("\nAfter changing age:")
print(person)