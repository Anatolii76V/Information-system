import office as cab
import student as si


def restart():
    choice = input('Хотите продолжить нажмите Y если нет то N ')
    if choice.upper() == 'Y':
        option()
    elif choice.upper() == 'N':
        print('До свидание.')
    else:
        restart()


def option():
    global index
    print("\nЭто программа для отслеживания процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(
            f'{si.stud_card["ID"][index]}, {si.stud_card["Имя"][index]},'
            f'{si.stud_card["Фамилия"][index]}\n,{si.stud_card["Дата рождения"][index]},'
            f' {si.stud_card["Успеваемость"][index]}')
        restart()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(
                f" Находится в классе - {cab.class_card['Предмет'][index]},"
                f"\n за партой № - {cab.class_card['Номер парты'][index]},  {cab.class_card['Ряд'][index]},"
                f" вариант - {cab.class_card['Вариант'][index]}, Имя: {si.stud_card['Имя'][index]},"
                f" Фамилия - {si.stud_card['Фамилия'][index]},\n  Успеваемость у студента:"
                f" {si.stud_card['Успеваемость'][index]}")
        restart()

    elif ch == 3:
        print('Вы вышли')
        exit()
    else:
        print('Не правильный выбор')


option()
