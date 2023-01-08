def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


while True:

    operation_sign = input("+ = adunare\n"
                           "- = scadere\n"
                           "* = inmultire\n"
                           "/ = impartire\n"
                           "c = opreste programul\n"
                           "Introduceti semnul de operare: ")

    if operation_sign == "c":
        break

    if operation_sign not in ['+', '-', '/', '*']:
        print("Nu a-ti introdus semnul de operare corect")
        continue

    first_number = float(input("Introduceti primul numar: "))
    second_number = float(input("Introduceti al doilea numar: "))

    if operation_sign == "+":
        print("Rezultatul este:", addition(first_number, second_number))
    elif operation_sign == "-":
        print("Rezultatul este:", substraction(first_number, second_number))
    elif operation_sign == "/":
        if second_number == 0.0:
            print("Impartirea la 0 nu se poate efectua")
        else:
            print("Rezultatul este:", division(first_number, second_number))
    elif operation_sign == "*":
        print("Rezultatul este:", multiplication(first_number, second_number))
    else:
        print("Nu a-ti introdus semnul de operare corect")

print()

"""Mult mai bine decat prima varianta de calculator. Bravo!

ce am mai observat:
- daca introduc o litera atunci cand trebuie sa inserez numar programul crapa. Ar trebui validat si asta:

Introduceti semnul de operare: -
Introduceti primul numar: 12
Introduceti al doilea numar: a
Traceback (most recent call last):
  File "/home/mihai/Mihai/records sciit/cursuri/Repo grupa 14/Repo Studenti Grupa 14/Burdetiu Samuel/Teme/Tema Calculator Functii.py", line 34, in <module>
    second_number = float(input("Introduceti al doilea numar: "))
ValueError: could not convert string to float: 'a'

"""