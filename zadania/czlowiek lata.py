DogAge = input('wiek psa w latach to: ')
DogAge1 = int(DogAge) * 10.5
DogAge2 = int(DogAge) - 2
DogAge3 = int(DogAge) - int(DogAge2)

if int(DogAge1) >= 1:
    print('wiek psa w ludzkich latach to : ', DogAge1)
else:
    sum = (int(DogAge3) * 10.5) + (int(DogAge2) * 4)
    print('wiek psa w ludzkich latach to: ',sum)
