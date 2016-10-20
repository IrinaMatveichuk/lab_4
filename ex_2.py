#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'a', 'A']
data2 = gen_random(1, 3, 10)

for i in Unique(data2, ignore_case = False):
    print(i)

