import random

x = random.randint(1, 100)

user = int(input("Palun sisestage number: "))

while True:
    if user > x:
        print("Arv on liiga kõrge")
        user = int(input("Palun sisestage number: "))
    elif user  < x:
        print("Arv on liiga madal")
        user = int(input("Palun sisestage number: "))
    else:
        break
print("Õige!")



