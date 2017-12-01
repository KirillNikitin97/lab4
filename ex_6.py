import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]

with open("data_light_cp1251.json", encoding="cp1251") as f:
    data = json.load(f)

#with open(path, encoding="cp1251") as f:
#    data = json.load(f)

@print_result
def f1(arg):
    return sorted(unique(field(arg, 'job-name'), ignore_case=1), key=lambda x: x.lower())

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))  # arg уменьшилось по предыдущему фильтру

@print_result
def f4(arg):
    s = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб.'.format(arg, s) for arg, s in zip(arg, s))

with timer():
    f4(f3(f2(f1(data))))
