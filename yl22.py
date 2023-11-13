import random

choices = ["kivi", "paber", "käärid"]
x = random.choice(choices)

while True:
    a = input("Sisesta kivi, paber või käärid(lõpetamiseks x): ")

    if a == "kivi" and x == "käärid" or a == "paber" and x == "kivi" or a == "käärid" and x == "paber":
        print("Sinu võit!")
    elif a == "kivi" and x == "paber" or a == "paber" and x == "käärid" or a == "käärid" and x == "kivi":
        print("Sina kaotasid")
    else:
        print("Viik")

    if a == "x":
        break