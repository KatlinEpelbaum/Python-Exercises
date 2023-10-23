a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

if a + b > c and a + c > b and b + c > a:
     print("Sellist kolmnurka ei eksisteeri.")

if a == b == c:
    print("Võrdkülgne kolmnurk")
elif a == b or a == c or b == c:
    print("Võrdhaarne kolmnurk")
else: 
    print("Erikülgne kolmnurk")
    