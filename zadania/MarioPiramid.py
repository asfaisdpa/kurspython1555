height = input('wysokosc piramidy to: ')
heightX = int(height) + 1
space = ' '
block = '#'
for i in range(1,int(heightX)):
    print((int(height) - i) * space,(i + (i-1)) * block)