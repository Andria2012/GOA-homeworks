# მოსწავლის dictionary
student = {
    "name": "Giorgi",
    "surname": "Lomidze",
    "age": 16,
    "subject": "Math"
}

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

student["age"] = 17
print("\nAfter changing age:")
print(student)

del student["subject"]
print("\nAfter deleting subject:")
print(student)

student.clear()
print("\nAfter clear():")
print(student)

student = {
    "name": "Giorgi",
    "surname": "Lomidze",
    "age": 16,
    "subject": "Math"
}

student.pop("surname")
print("\nAfter pop surname:")
print(student)