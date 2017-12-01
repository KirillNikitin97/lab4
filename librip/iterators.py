# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items) if isinstance(items, list) else items  # проходим по элементам
        self.ignore_case = kwargs.get('ignore_case', False)  # По-умолчанию ignore_case = False
        self.lst = set()

    def __next__(self):
        while True:
            el = next(self.items)
            if self.ignore_case:
                if el.lower() not in self.lst:
                    self.lst.add(el.lower())
                    return el
            elif el not in self.lst:
                self.lst.add(el)
                return el

    def __iter__(self):
        return self

