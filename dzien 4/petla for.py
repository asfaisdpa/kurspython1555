magic = 'abracadabra'
vowels = 'a'
vowels_counter = 0
consonants = 'brcd'
consonants_counter = 0

for char in magic:
    if char in vowels:
        vowels_counter += 1
    elif char in consonants:
        consonants_counter += 1
    else:
        continue
    print('char', char)
print('ilosc samoglosek',vowels_counter)
print('ilosc spolglosek',consonants_counter)