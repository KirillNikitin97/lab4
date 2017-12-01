import random


def field(items, *args):
    assert len(args) > 0, 'No arguments'
    i = 0
    if len(args) == 1:
        while i < len(items):
            if items[i].get(args[0]) is not None:
                yield items[i].get(args[0])
            i += 1
    else:
        while i < len(items):
            d = {}
            for el in args:
                if items[i].get(el) is not None:
                    d[el] = items[i].get(el)
            if len(d) != 0:
                yield d
            i += 1


def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin,end)
