a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Sellist kolmanurka pole olemas")
elif a == b and b==c:
    print("Võrdkülgne kolmnurk")
elif a == b and b != c or a == c and a != b or b == c and b != a:
    print("Võrdhaarne kolmnurk")
else:
    print("Erikülgne kolmnurk") 