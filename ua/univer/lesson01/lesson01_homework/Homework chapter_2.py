# 1. Программа, которая выводит приведенну. ниже личную информацию
name=input('Ваше имя ')
region=input('Ваш адрес проживания сгородом, областью и почтовым индексом ')
phone=input('Ваш номер телефона ')
spel=input('Ваша специализация в учебном заведении ')
print(name,region,phone,spel)
# 2. Прогноз продаж
Planov_sum=int(input('Введите плановую сумму продаж '))
pribul= float(Planov_sum*0.23)
print(Planov_sum,pribul)
# 3. Расчет площади замельного участка (перепроверить)
General_square =int(input('Введите количество квадратных метров земли '))
number_of_akr= float(General_square / 4047)
print(General_square,number_of_akr)
# 4. Общий объем продаж
price_1 =float(input('Введите цену первого товара '))
price_2 =float(input('Введите цену второго товара '))
price_3 =float(input('Введите цену третьего товара '))
price_4 =float(input('Введите цену четвертого товара '))
price_5 =float(input('Введите цену пятого товара '))
overal_price=(price_1+price_2+price_3+price_4+price_5)
price_with_tax=(price_1+price_2+price_3+price_4+price_5)*0.07
print(price_1,price_2,price_3,price_4,price_5)
print(overal_price)
print(price_with_tax)
# 5. Пройденное расстояние
distance_1=(70*6)
distance_2=(70*10)
distance_3=(70*15)
print(distance_1,distance_2,distance_3)
# 6. Налог с продаж
price=float(input('Введите cумму покупки '))
federal_tax=0.05
redional_tax=0.025
general_tax=federal_tax+redional_tax
overal_price_with_tax=(price*(general_tax))
print(price)
print(federal_tax)
print(redional_tax)
print(general_tax)
print(overal_price_with_tax)
# 7. расход= пройденные киломентры /расход бензина в литрах
kilometers_traveled=int(input('Введите пройденные километры '))
consumption_petrol =int(input('Введите расход бензина '))
consumption=kilometers_traveled/consumption_petrol
print(kilometers_traveled,consumption_petrol,consumption)
# 8. Чаевые налог и общая сумма
price=float(input('Введите cумму заказа '))
tips=price*0.18
tax=price*0.07
general_price=price+tips+tax
print(price,tips,tax,general_price)
#9. Преобразование темпираторы по шкале Цельсия в темпиратору по шкале Форенгейта
temp_cels=float(input('Введите темпиратору по шкале Цельсия '))
temp_farengeit=((9/5)*temp_cels)+32
print(temp_cels,temp_farengeit)
#10 Регулятор ингредиентов

#11 Процент учащихся обоего пола
gils=int(input('Cколько девочек учится в классе '))
boys=int(input('Cколько мальчиков учится в классе '))
general=gils+boys
gils_proportion=gils/general
boys_proportion=boys/general
print(gils,boys,gils_proportion,boys_proportion)
#12 Программа расчета купли-продажи акций
bought_price=(2000*40.00)*0.03
sold_price=(2000*42.75)*0.03
profit=sold_price-bought_price
print(bought_price,sold_price,profit)
#13 Выращивание винограда
ridge_lengt_R=int(input('Введите длину гряды '))
volume_E=int(input('Введите обьем пространства, занимаемого концевыми опорами '))
volume_S=int(input('Введите обьем пространства между виноградными лозами в метрах'))
number_of_vines=(ridge_lengt_R-(2*volume_E))/volume_S
print(ridge_lengt_R,volume_E,volume_S,number_of_vines)
#14 Сложный процент
deposit_amount_P=int(input('Укажите сумму вклада, внесенную на сберегатльный фонд '))
vannual_rate_r=float(input('Внесите годовую процентую ставку,начислемую на остаток счета '))
frequency_of_accrual_n=int(input('Внесите частоту начисления процентного дохода '))
number_of_years_t=int(input('Введите количество лет в течении которого сберегатльный фонд будет зарабатывать '))
amount_of_money=deposit_amount_P*(1+(vannual_rate_r/frequency_of_accrual_n))*frequency_of_accrual_n*number_of_years_t
print(deposit_amount_P,vannual_rate_r,frequency_of_accrual_n,number_of_years_t,amount_of_money)


