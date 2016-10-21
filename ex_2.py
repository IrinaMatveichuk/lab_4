#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators_2 import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'Aaa', 'aaa', 'aAa', 'Aaa', 'AAa', 'aAA', 'AAA', 'aaa']
data2 = gen_random(1, 3, 10)

for i in Unique(data1, ignore_case = False):
    print(i)

