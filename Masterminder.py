#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
print('Zapraszam do gry mastermind. "Wpisz start"')
A = input()
if A == "start":
    print("Zaczynamy!!!!")
if A == "stop":
    print("spadaj")

list = [1, 2, 3, 4, 5, 6]
c = random.choice(list)
d = random.choice(list)
e = random.choice(list)
f = random.choice(list)

copa = c,d,e,f
list1 = [c, d, e,f]

for list1 in range(0, 5):
    odp = input()





