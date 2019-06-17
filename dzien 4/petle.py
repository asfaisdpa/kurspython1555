# pobierz od uzoykownika dowolna calkowita liczba


value = int(input())

counter = 0
iteration_no = 0

while counter < value:
    iteration_no += 1
    print('Python', iteration_no)
    # counter += 1   # skrocenie zapisu counter = counter + 1
    if  iteration_no == 100:
        break
