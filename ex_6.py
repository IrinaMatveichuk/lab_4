#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]

with open(path, encoding="utf8") as f:
    data = json.load(f)

@print_result
def f1(data):
    a = (el for el in field(data, 'job-name'))
    b = (el for el in unique(a, ignore_case = True))
    return sorted(b)

@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x, arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    salary = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб.'.format(ar, sal) for ar, sal in zip(arg, salary))

with timer():
    f4(f3(f2(f1(data))))
