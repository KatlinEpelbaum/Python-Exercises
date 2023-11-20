import random

x = random.randint(1, 100)

user = int(input("Palun sisestage number: "))

while x != user:
    if user > x:
        print("Arv on liiga kõrge")
    elif user < x:
        print("Arv on liiga madal")
    user = int(input("Palun sisestage number: "))
print("Õige!")



