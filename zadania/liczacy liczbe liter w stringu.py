numbers = 0
others = 0  #letters and other

string = input()

for i in string:
    if i.isdigit():
        numbers += 1
    elif i.isdigit != True:
        others += 1

print('tyle mamy liczb: ',numbers)
print('tyle mamy liter i innych znakow: ',others)

import string
string.