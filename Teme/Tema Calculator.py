# Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
#
# - calculatorul detine cifre de la 0 la 9,
#
# - semnele matematice cu ajutorul carora se vor putea realiza operatii matematice sunt urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
#
# - pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul litere C
#
# - toate operatiile presupun interactiunea cu utilizatorul (functii de tip input)

while True:

        operation_sign = input("+ = adunare\n"
                               "- = scadere\n"
                               "* = inmultire\n"
                               "/ = impartire\n"
                               "c = opreste programul\n"
                               "Introduceti semnul de operare: ")

        if operation_sign == "c":
            break

        first_number = float(input("Introduceti primul numar: "))
        second_number = float(input("Introduceti al doilea numar: "))
        if operation_sign == "c":
            break

        if operation_sign == "+":
            print(first_number + second_number)
        elif operation_sign == "-":
            print(first_number - second_number)
        elif operation_sign == "/":
            print(first_number / second_number)
        elif operation_sign == "*":
            print(first_number * second_number)
        else:
            print("Nu a-ti introdus semnul de operare corect")

print()