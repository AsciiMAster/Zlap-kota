#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

lista = ["1", "2", "3", "4", "5", "6", "7", "8"]

wyb1 = random.choice(lista)
wyb2 = random.choice(lista)
wyb3 = random.choice(lista)
wyb4 = random.choice(lista)

wybor_komp = [wyb1, wyb2, wyb3, wyb4]
print(wybor_komp)

def cala():
 print("Witaj w grze masterminder wybierz 4. ")
 print("Wybierz 4 liczby:")
 wybor_user = list(input())
 print(wybor_user)

 odrzucone_user = []
 odrzucone_komp = []

 for pozycja in range(4) :
	 if wybor_user[pozycja] == wybor_komp[pozycja] :
		 print("x")
	 else:
		 odrzucone_user.append(wybor_user[pozycja])
		 odrzucone_komp.append(wybor_komp[pozycja])

 for odrzucone_komp in odrzucone_user:
	 if odrzucone_komp in odrzucone_komp:
		 print("O")
	 else:
		 odrzucone_komp_user.append(odrzucone_komp)
cala()

