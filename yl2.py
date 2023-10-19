import math

radius = float(input("Sisesta Raadius: "))

area = radius * radius * math.pi
circumference = 2 * math.pi * radius 

area = round(area, 2)
circumference = round(circumference, 2)

print ("Ringi pindala:", (area))
print ("Ringi ümbermõõt:", (circumference))