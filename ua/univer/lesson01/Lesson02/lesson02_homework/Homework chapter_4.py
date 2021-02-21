# 1. Сборщик ошибок
MAX=5
total=0.0
print('Эта программа вычисляет сумму ошибок за 5 дней')
for counter in range (MAX):
    number=int(input('Введите количество ошибок за день: ' ))
    total=total+number
    print('Cумма составялет: ', total)
# 2. Cожженные колории
# Эта программа выводит количество колорий, сожженных после 10,15, 20, 25, 30 минут
START_MINUTS=10
END_MINUTS=35
INTERVAL=5
СALORIES=4.2
for number in range(START_MINUTS,END_MINUTS,INTERVAL):
    number_calories=number* СALORIES
    print("Количество колорий: ", number, number_calories)
# 3. Анализ бюджета

# 4. Пройденное растояние
speed = int(input('Какая скорость транспортного средства в км/ч: '))
hours = int(input('Сколько часов оно двигалось: '))
start=1
end=hours+1
interval=1
total=0.0
print('hours', '\t', 'distance')
print('________________')
for h in range (start, end, interval):
        distance = (speed * hours) / hours
        total = total + distance
        print(h,total)
# 5. Средняя толщина дождевых осадков
# 6. Таблица соответствия между градусами Цельсия и градусами Фаренгейта
Min=1
Max=20
interval=1
total=0.0
c = int(input('Введите темпиратуру в Цельсиях (от 1 до 20): '))
for h in range (Min, Max, interval):
        Forengeyt = ((9/5)*c)+32
        total = total + Forengeyt
        print(h,total)
# 7. Мелкая манета для зарплаты
n = int(input('Введите количество отработанных дней: '))
Min=1
Max=n
interval=1
total=0.0
for d in range(Min,Max+1,interval):
    salary_c = (n * 1)/n
    total = total + salary_c
    print(d, 'Деньги в капейках за день: ', format(total, '.2f'))
    salary_m= total/100
    print(d, 'Деньги в рублях: ' , format(salary_m, '.2f'))
#8. Cумма чисел


