print('witaj w kalkulatorze. Jakie tryb wybrać "dodawanie" czy "średnia"?')
odp = input()
print()
if odp == "dodawanie" :
    print("podaj dwie liczby które chcesz dodać")
    liczba1 = int(input())
    liczba2 = int(input())
    wynik1 = liczba1 + liczba2
    print("oto twój wynik", wynik1)
if odp == "srednia" :
    print("podaj dwie liczby dla średniej")
    liczba3 = int(input())
    liczba4 = int(input())
    wynik2 = (liczba3 + liczba4) / 2
    print("twój wynik to:", wynik2 )
else :
    print("ten kalkulator nie jest tak zaawansowany")