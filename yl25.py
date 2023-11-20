dictionary = {
    "eesnimi": "Kätlin",
    "perenimi": "Epelbaum",
    "sünniaasta": 2006,
    "elukoht": "Kuressaare",
    "lemmik loom": "kass"
}
m = dictionary.get("elukoht")
print(m)
print(dictionary["elukoht"])

dictionary["lemmik loom"] = "Kassid ja rotid"

print(dictionary.keys())

for i in dictionary.values():
    print(i)

if "isikukood" in dictionary:
    print("Eksisteerib")
else:
    print("Ei eksisteeri")

print(len(dictionary))

dictionary["pikkus"] = 165

del dictionary["sünniaasta"]
print(dictionary)


