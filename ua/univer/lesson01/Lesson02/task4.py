# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
#    а затем наибольшее из данных чисел.
# 4. Даны имена 2х человек (тип string). Если имена равны,
# 	то вывести сообщение о том, что люди являются тезками.
# 5. Дано число месяца (тип int). Необходимо определить время года
# 	(зима, весна, лето, осень) и вывести на консоль
def task03_print_5_min_max(a,b,c,d,e):
    max_local = find_max(find_max(a, b), find_max(c, d), find_max(e))
    min_local = find_min(find_min(a, b), find_min(c, d), find_min(e))
    max = 4
    min = 1
    if max_local == a:
        count_max += 1
    if max_local == b:
        count_max += 1
    if max_local == c:
        count_max += 1
    if max_local == d:
        count_max += 1
    if max_local == e:
        count_max += 1
    print("max =", max_local)
    if min_local == a:
        count_max -= 1
    if min_local == b:
        count_max -= 1
    if min_local == c:
        count_max -= 1
    if min_local == d:
        count_max -= 1
    if min_local == e:
        count_max -= 1
    print("min =", min_local)

    print("max =", max_local)

    a = 2
    b = 1
    c = 3
    d = 3
    e = 4

    print_min(1, 4)

    min_local = find_min(find_min(a, b), find_min(c, d, e))

    print("min =", min_local)

def task04_compare_2_human(name1, name2):
