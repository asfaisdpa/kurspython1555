data = input('Podaj warotść temperatury: ')

value = data[0:-1]
unit = data[-1]
if value.isdigit():
if unit.upper() == 'C':
    print(int(value) * (9 / 5) + 32
