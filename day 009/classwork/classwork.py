hour = int(input("შეიყვანე საათი: "))

if hour < 10:
    print("დილამშვიდობისა")
elif hour < 20:
    print("საღამო მშვიდობისა")
else:
    print("ღამე მშვიდობისა")

temperature = int(input("შეიყვანე ტემპერატურა: "))

if temperature < 0:
    print("ცივა")
elif temperature < 15:
    print("გრილა")
else:
    print("ცხელა")

score = int(input("შეიყვანე ქულა: "))

if score > 90:
    print("ყოჩაღ")
elif score < 50:
    print("უკეთესი შეიძლება")
else:
    print("ჩაიჭერი")