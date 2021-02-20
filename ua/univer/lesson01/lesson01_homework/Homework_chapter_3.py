# 1. День недели. Программа должн вывести сообщение об ошибке, если пользователь вводит сообшение вне диапозона
x = int(input("Введите число: "))
if x >= 1 and x < 8:
    print('Зачение лежит в допустимом диапозоне')
else:
    print('Зачение лежит в недопустимом диапозоне')
# 2. Площать прямоуголников: вывести сообщение площадь какого прямоуголника больше или сообщить об ошибке
length_1 = int(input("Введите длину первого прямоуголника: "))
width_1 = int(input("Введите ширину первого прямоуголника: "))
length_2 = int(input("Введите длину второго прямоуголника: "))
width_2 = int(input("Введите ширину второго прямоуголника: "))
square_1=length_1*width_1
square_2=length_2*width_2
if square_1 > square_2:
    print("Площадь первого прямоуголника больше")
if square_2 > square_1:
        print("Площадь второго прямоуголника больше")
if square_1 == square_2:
        print("Площадь прямоугольников равна")
# 3. Классификатор возраста:
age = int(input("Введите Ваш возраст: "))
if age <= 1:
    print("Младенец")
if age > 1 and age <= 13:
        print("Ребенок")
if age >= 13 and age <= 20:
        print("Подросток")
if age > 20 :
        print("Взрослый")
# 4. Римские цифры
number = int(input("Введите число: "))
if number == 1:
    print("I")
else:
    if number == 2:
        print("II")
    else:
        if number == 3:
            print("III")
        else:
            if number == 4:
                print("IV")
            else:
                if number == 5:
                    print("V")
                else:
                    if number == 6:
                        print("VI")
                    else:
                        if number == 7:
                            print("VII")
                        else:
                            if number == 8:
                                print("VIII")
                            else:
                                if number == 9:
                                    print("XI")
                                else:
                                    if number == 10:
                                        print("X")
                                    else:
                                            print("Неизвестно")
#5. Масса и вес Если вес тела больше 500 Н - тело слишком тяжелое, меньше 100 - тело слишком лгкое
weight = float(input("Введите массу тела: "))
weight_newton=weight*9.8
if weight_newton > 500:
    print("Тело слишком тяжелое")
elif weight_newton < 100:
    print("Тело слишком легкое")
else:
        print("В пределах нормі")
#6.Волшебные даты
month = int(input("Введите месяц в числовой форме: "))
day = int(input("Введите день: "))
year = int(input("Введите двузначный год: "))
product_of_numbers=month*day
if product_of_numbers == year:
    print("Данная дата является волшебной: ")
else:
    print("Дата не является волшебной")
# 7. Цветовой микшер
сolor_1 = input("Введите название одного цвета с маленькой буквы: ")
сolor_2 = input("Введите название второго цвета с маленькой буквы: ")
if сolor_1 == "красный" and сolor_2 == "синий" or сolor_1 =="синий" and сolor_2 == "красный":
    print("фиолетовый")
elif сolor_1 == "красный" and сolor_2 == "желтый" or сolor_1 =="желтый" and сolor_2 == "красный":
    print("оранжевый")
elif сolor_1 == "синий" and сolor_2 =="желтый" or сolor_1 =="желтый" and сolor_2 == "синий":
    print("зеленый")
else:
    print("ошибка")
# 8. Калькулятор сосисок для пикника
people = int(input('kolvo ludei? '))
hotdog_na_chel = int(input('skolko hotdogov kagdomy? '))
all_hotdogs = people * hotdog_na_chel

if all_hotdogs <= 10:
    sos_upak = 1
    bul_upak = 1

    sos_ostal = 10 - allhotdogs
    bul_ostal = 8 - allhotdogs
elif all_hotdogs > 10:
    upak_sos = (all_hotdogs // 10) + 1 < +1
    про
    который
    говорил
    upak_bul = (all_hotdogs // 8) + 1 < +1
    про
    который
    говорил

    sos_ostal = upak_sos * 10 - all_hotdogs
    bul_ostal = upak_bul * 10 - all_hotdogs
print(upak_sos, upak_bul, sos_ostal, bul_ostal)




