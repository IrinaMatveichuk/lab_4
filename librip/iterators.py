class Unique(object):
    new_list = []
    def __init__(self, items, **kwargs):
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = kwargs.get('ignore_case', "False")
        self.items = iter(items) if isinstance(items, list) else items

    def __next__(self):
        for el in self.items:
            if self.ignore_case == False and type(el) != int:
                if self.new_list.count(el.upper()) == 0:
                    self.new_list.append(el.upper())
                    return el
                else: continue
            else:
                if self.new_list.count(el) == 0:
                    self.new_list.append(el)
                    return el
                else: continue
        raise StopIteration

    def __iter__(self):
        return self