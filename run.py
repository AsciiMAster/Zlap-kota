#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""\
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-

Witaj w programie złap kota. 

     Wpisz "start" jeśli chcesz zacząć   |   Wpisz "opcje" jeśli chcesz opcje      

""")


odp = input()
if odp == "start":
    print('dobrze zaczynajmy weź ze sobą siatkę wpisując "siatka" ')
if odp == "opcje":
    print("""
     
         _
      |/'/-..--.
     / _ _   ,  ;
    `~=`Y'~_<._./
    <`-....__.' 
    
    Na razie nic tu nie ma.
    """)
tlip = input()
if tlip == "siatka":
    print('''"
           _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm
    "''')
if tlip == "nie":
    print("test1")
import random
list = ["kuchnia", "strych", "magazyn", "pokuj dziecięcy", "sypialnia", "przedpokuj", "garaż", "akwarium"]
print("kot znajduje się w:", random.choice(list) ,"złap go!!!!!!!!!")
choice = random.randint(1, 20)
if choice == choice < 10:
    print("złapałeś i wygrałeś")
if choice == choice > 10:
    print("uciekł")
koniec = input()
if koniec == "tak":
       print("""
           +--------------+ 
          /|             /|
         / |            / |
        *--+-----------*  |
        |  |           |  |
        |  |           |  |
        |  |           |  |
        |  +-----------+--+
        | / Jakub fisch| /er
        |/             |/
        *--------------*
 Autor:   Jakub fischer

zacznij jeszcze raz
""")





