print('hello world')
print ('to jest kalkulator sumowania')


def sumuj(liczba1, liczba2):
    return liczba1 + liczba2


a = int(input("Podaj liczbe A: "))
b = int(input("Podaj liczbe B: "))

print()
wynik = sumuj(a, b)
print("%s + %s = %s" % (a, b, wynik))
