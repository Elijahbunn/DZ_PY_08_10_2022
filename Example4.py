X = int(input('Введите номер четверти: '))

if X == 1:
    print('x = (0; +infinity)')
    print('y = (0; +infinity)')
if X == 2:
    print('x = (0; -infinity)')
    print('y = (0; +infinity)')
if X == 3:
    print('x = (0; -infinity)')
    print('y = (0; -infinity)')
if X == 4:
    print('x = (0; +infinity)')
    print('y = (0; -infinity)')

elif (X != 1 & X != 2 & X != 3 & X != 4):
    print('Введите номера от 1 до 4') 