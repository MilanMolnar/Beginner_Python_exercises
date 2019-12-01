import time
import sys


def sprint(str):  # Sprint function definialasa, hogy lassan irja ki a pontokat.
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.8 / 1)


print("Kilepeshez ird be, hogy \"exit\". ")
z = input('Ird be az operatort a muvelet megkezdesehez: ')  # operator bekerese.
if z == "exit":
    print("kilepes")  # Teszt 0-ra valo kilepes
    exit()


def get_number_from_console(parameter):
    value = None
    while True:
        try:
            value = float(input(parameter))
        except ValueError:
            print("Kerkek szamot adj meg!")
            continue

        if isinstance(value, float):
            break
    return value

x = get_number_from_console("Adj meg egy szamot: ")
y = get_number_from_console("Adj meg egy másik szamot: ")

try:  # Nullaval valo osztas hiba kezelese
    if z in ("+", "-", "*", "/"):  # Operator validalasa
        if z == "+":  # Operator kivalasztas
            print("A szamolas eltarthat par masodpercig.")
            sprint("...")
            print("Eredmeny = ", x + y)  # Muvelet elvegzese

        elif z == "-":
            print("A szamolas eltarthat par masodpercig.")
            sprint("...")
            print("Eredmeny = ", x - y)

        elif z == "*":
            print("A szamolas eltarthat par masodpercig.")
            sprint("...")
            print("Eredmeny = ", x * y)

        elif z == "/":
            print("A szamolas eltarthat par masodpercig.")
            sprint("...")
            print("Eredmeny = ", x / y)
    else:
        print("Nem megfelelo operator")
except:
    print("Nullával nem lehet osztani!")
