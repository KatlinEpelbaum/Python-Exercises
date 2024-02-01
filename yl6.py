a = input("Sisesta arv a: ")
b = input("Sisesta arv b: ")
c = input("Sisesta arv c: ")

if int(a)> int(b) and int(a)> int(c):
    print(a, "on suurem kui", b, ",", c)
   
elif int(b) > int(c) :
    print(b, "on suurem kui", a, ",", c)
    
else:
    print(c, "on suurem kui", a, ",", b)