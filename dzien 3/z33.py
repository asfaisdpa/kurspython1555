data = input('podaj wartosc temperatur: ')

value = data[0:-1]
unit = data[-1]

if value.isdigit():
    value_converted = int(value)

    if unit.upper() == 'C':
        value_farenheit = value_converted * (9/5) + 32
        print(f'temperatura w Farenheitach wynosci: {value_farenheit}')
    elif unit.upper() == 'F':
        value_celcius = (value_converted - 32) * (5/9)
        print(f'temperatura w celciuszach wynosci : {value_celcius}')
    else:
        print('podaj warosc w celciuszach lub farenheitach')

else: print('podaj poprawna wartosc')