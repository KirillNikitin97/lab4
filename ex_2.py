
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a','P','k','M','A','p','m']

# Реализация задания 2
print('Before Unique',data1)
u1 = Unique(data1)
print('After Unique', end = ' ')
for i in u1:
    print(i, end=" ")
print('\nC ГЕНЕРАТОРОМ\nBefore Unique')
d2=[]
for i in data2:
    d2.append(i)
    print(i, end=" ")
print('\nAfter Unique')
u2 = Unique(d2)
for k in u2:
    print(k, end=" ")
print()


print('Before Unique',data3)
u3 = Unique(data3)
for i in u3:
    print(i, end=" ")
print()

print('Без повторений по регистру:')
u4 = Unique(data3, ignore_case = True)
for i in u4:
    print(i, end=" ")
