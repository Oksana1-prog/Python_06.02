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

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

def print_min(x,y):
    if x < y:
        mymin = x
    else:
        mymin = y
    print("mymin =", mymin)

a = 2
b = 1
c = 3
d = 3

print_min(10,20)

min_local = find_min(find_min(a,b),find_min(c,d))

print(min_local)


def find_max(x,y):
    if x > y:
        return x
    else:
        return y

def print_max(x,y):
    if x > y:
        mymax = x
    else:
        mymax = y
    print("mymax =", mymax)

a = 2
b = 1
c = 3
d = 3