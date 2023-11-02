user = input("Sissestage lause: ")

if len(user) >= 7 and not len(user) % 2:
 print(user.strip())
 number = len(user)
 middle = int((number- 1) // 2)
 print (user [middle])
 print (user [middle + 1])
 print (user [middle + 2])

else:
    print("Sümboleid peab olema rohkem kui 7, paaritus arvus")

