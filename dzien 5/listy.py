# uzytkownik podaje nam na wejscu 2 liczby,
#
num1 = input()
num2 = input()
# index = int(input())
#
lista = list(range(int(num1),int(num2)))
#
# print(lista[index])

lf = int(input())
found = False

for i in lista:
    if i == lf:
        print('w liscie jest wartosc: ',lf)
        found = True
        break
if not found:
    print('nie ma tego w liscie')




