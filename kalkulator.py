print ('to jest kalkulator sumowania i odejmowania')


def sumuj(liczba1, liczba2):
    return liczba1 + liczba2

def odejmowanie(liczba1, liczba2):
    return liczba1 - liczba2


a = int(input("Podaj liczbe A: "))
b = int(input("Podaj liczbe B: "))

print()
wynik = sumuj(a, b)
wynik2 = odejmowanie(a, b)
print("%s + %s = %s" % (a, b, wynik))
print("%s - %s = %s" % (a, b, wynik2))
