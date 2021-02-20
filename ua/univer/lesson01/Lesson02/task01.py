# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль
def find_min(x,y)
    if x < y:
        return x
    else:
        return y

a=1
b=2
c=3
d=4
min_local=a
if b<min_local:
    min_local=b
if c<min_local:
    min_local=c
if d < min_local:
        min_local = d
print(min_local)

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

a = 2
b = 1
c = 3
d = 3

min_local1 = find_min(a,b)
min_local2 = find_min(c,d)
min_local = find_min(min_local1,min_local2)

print(min_local)

# 2. Вывести на консоль количество