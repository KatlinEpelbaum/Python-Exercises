user = input("Sissestage lause: ")
length = len(user)
middle = int((length - 1) // 2)
if (length >= 7) and not (length % 2) == 0:
    print(user.strip())
    print (user [middle - 1])
    print (user [middle])
    print (user [middle + 1])

else:
    print("Sümboleid peab olema rohkem kui 7, paaritus arvus")
