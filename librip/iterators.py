# Итератор для удаления дубликатов
class Unique(object):
    i = -1
    new_list = []
    def __init__(self, items, **kwargs):
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        try:
            self.ignore_case = kwargs['ignore_case']
        except: self.ignore_case = False
        self.items = items
        self.index = 0
        if (type(self.items) != list):
            gen = self.items
            self.items = []
            for el in gen:
                self.items.append(el)
        self.index = len(self.items)

    def __next__(self):
        self.i += 1

        if (self.i == self.index):
            raise StopIteration

        fl = False
        if (self.ignore_case == False and type(self.items[self.i]) != int):
            if (self.new_list.count(self.items[self.i].upper()) == 0 and self.new_list.count(self.items[self.i].lower()) == 0):
                self.new_list.append(self.items[self.i])
                self.fl = True
                return self.items[self.i]
            else: return self.__next__()
        else:
            if (self.new_list.count(self.items[self.i]) == 0):
                self.new_list.append(self.items[self.i])
                self.fl = True
                return self.items[self.i]
            else: return self.__next__()

    def __iter__(self):
        return self
