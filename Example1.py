dayN = int(input('Введите номер недели: '))

if dayN == 1:
        print("Понедельник - будний день")
if dayN == 2:
        print("Вторник - будний день")
if dayN == 3:
        print("Среда - будний день")
if dayN == 4:
        print("Четверг - будний день")
if dayN == 5:
        print("Пятница - будний день")
if dayN == 6:
        print("Суббота - выходной день")
if dayN == 7:
        print("Воскресенье - выходной день")

elif (dayN != 1 & dayN != 2 & dayN != 3 & dayN != 4 & dayN != 5 & dayN != 6 & dayN != 7):
    print("Введите номер от 1 до 7")
    