dictionary = {
    "name": "Kätlin",
    "last_name": "Epelbaum",
    "birth_year": 2006,
    "location": "Kuressaare",
    "favorite_animal": "kass"
}
m = dictionary.get("location")
print(m)
print(dictionary["location"])

dictionary["favorite_animal"] = "Kassid ja rotid"

print(dictionary.keys())

for i in dictionary.values():
    print(i)

if "isikukood" in dictionary:
    print("Eksisteerib")
else:
    print("Ei eksisteeri")

print(len(dictionary))

dictionary["height"] = 164

del dictionary["birth_year"]
print(dictionary)


