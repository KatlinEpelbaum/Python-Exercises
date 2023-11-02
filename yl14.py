file = input("Sisestage failinimi kujul .ext: ")
ext = file.split(".")
if ".ext" in file:
    print(ext[1])

else:
    print("Faili nimi pole kujul .ext")