import task_if_lib
a=2
b=1
c=3
d=3
task_if_lib.print_min(10,20)
min_local=task_if_lib.find_min(task_if_lib.find_min(a,b),task_if_lib.find_min(c,d))
print("min=",min_local)
task_if_lib.find_and_print_max_count()

# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
# а затем наибольшее из данных чисел.
def task03_print_5_min_max(a,b,c,d,e):
    pass
import task_if_lib
a=2
b=1
c=3
d=3
e=4
task_if_lib.print_min(10,20)
min_local=task_if_lib.find_min(task_if_lib.find_min(a,b),task_if_lib.find_min(c,d))
max_local=task_if_lib.find_max(task_if_lib.find_max(a,b),task_if_lib.find_max(c,d))
print("min=",min_local)
print("max=",max_local)
task03_print_5_min_max(a,b,c,d,e)







