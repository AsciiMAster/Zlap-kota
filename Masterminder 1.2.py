#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


# the .randrange() function generates a
# random number within the specified range.
num = random.randrange(1000, 10000)

n = int(input("Wybierz 4 liczby:"))


if (n == num):
	print("Dobrz. Wybrałeś za pierwszym razem jesteś Mastrerminderem")
else:

	ctr = 0

	while (n != num):

		ctr += 1

		count = 0


		n = str(n)

		num = str(num)

		correct = ['X']*4

		for i in range(0, 4):


			if (n[i] == num[i]):

				count += 1

				correct[i] = n[i]
			else:
				continue


		if (count < 4) and (count != 0):
			print("Nie te numery ale zaznaczyłeś ", count, " digit(s) dobrze!")
			print("3 mumerki były dobrze.")
			for k in correct:
				print(k, end=' ')
			print('\n')
			print('\n')
			n = int(input("Wpisz następne 4 liczby: "))


		elif (count == 0):
			print("Żadne liczby się nie zgadzają.")
			n = int(input("Wybierz 4 liczby: "))
	if n == num:
		print("Jesteś masterminderem!")
		print("zajęło ci to", ctr,)



