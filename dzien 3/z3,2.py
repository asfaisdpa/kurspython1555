post_code = input('podaj kod pocztowy: ')

post_code_splitted = post_code.split('-')

if post_code[0].isdigit() and post_code[1].isdigit():
    print('kod pocztowy jest poprawny')
else:
    print('kod pocztowy jest niepoprawny')



if post_code[:2].isdigit() and post_code[3:].isdigit():
    print('kod pocztowy jest poprawny')
else:
    print('kod pocztowy jest niepoprawny')


