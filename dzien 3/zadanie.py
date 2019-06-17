a = input('podaj liczbe: ')


if a.isdigit():
    a = int(a)

    if a % 3 == 0:
        print(int(a),'liczba jest podzielna przez 3')
    if a % 5 == 0:
        print(int(a),'liczba jest podzielna przez 5')
    if a % 7 == 0:
        print(int(a), 'liczba jest podzielna przez 7')

else:
    print("niepoprawne dane")
