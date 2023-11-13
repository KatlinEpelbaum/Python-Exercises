text = input("Sisesta tekst: ")
vowels = "aieouüõöAIEOUÜÕÄÖ"
count = sum(text.count(vowel) for vowel in vowels)
print(count)