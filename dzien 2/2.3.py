a = input('Podaj liczbe calkowita: ')
# a = int(a)  skrocenie wyzej

if a.isdigit():
    a = int(a)
    if a % 2:
        print(int(a), "jest nieparzyste")
    else:
        print(int(a), ' jest parzyste')
else:
    print('podales niepoprawne dane wejsciowe')