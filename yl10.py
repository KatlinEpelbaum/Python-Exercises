name = input("Palun sisestage nimi: ")
print("Tere", name, "!")

area = input("Palun sisestage elukoht: ")
if "saaremaa" in area.lower():
    print("Tere saarlane!")

age = int(input("Palun sisestage oma vanus: "))
if age < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne, sa oled täisealine!")
else:
    print("Sa võid autot juhtida!")