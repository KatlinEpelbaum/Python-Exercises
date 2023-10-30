fruitlist = ["Õun", "Banaan", "Pirn"]
print(fruitlist[0])

fruitlist.append("Kirss")
print(fruitlist[3])

fruitlist[0] = ("Mustikas")
print(fruitlist)

if "õun" in fruitlist:
    print("Õun on listis")

print(len(fruitlist))

fruitlist.remove("Pirn")
print(fruitlist)

fruitlist.reverse()
print(fruitlist)

fruitlist.sort()
print(fruitlist)