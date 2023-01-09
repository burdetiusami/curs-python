# Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
# - calculatorul detine cifre de la 0 la 9,
# - semnele matematice cu ajutorul carora se vor putea realiza operatii matematice
# sunt urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
# - pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul litere C
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

    first_number = (input("Introduceti primul numar: "))
    second_number = (input("Introduceti al doilea numar: "))
    if operation_sign == "c":
        break

    if first_number.isalpha() or second_number.isalpha():
        print('Introduceti doar numere')
        continue

    if operation_sign not in ['+', '-', '/', '*']:
        print("Nu a-ti introdus semnul de operare corect")
        continue
    elif operation_sign == "+":
        print(float(first_number) + float(second_number))
    elif operation_sign == "-":
        print(float(first_number) - float(second_number))
    elif operation_sign == "/":
        print(float(first_number) / float(second_number))
    elif operation_sign == "*":
        print(float(first_number) * float(second_number))
    else:
        print("Nu a-ti introdus semnul de operare corect")

print()


""" Daca nu introduc semnul de operare corect, programul ma lasa sa introduc mai departe primul numar si al doilea. 
Corect ar fi sa ma atentioneze de la inceput ca nu am introdus corect, nu la sfarsit. 

if operation_sign not in ['+', '-', '/', '*']:
    print("Nu a-ti introdus semnul de operare corect")
    continue
    
Daca nu introduc numar (introduc litere), programul crapa --> trebuie sa validam si sa atentionam utilizatorul ca nu a introdus
ce trebuie si deci trebuie sa repete instructiunea.
 
Daca incerc sa impart la 0, programul crapa (ar fi trebuit sa am mesaj ca nu se poate efectua impartirea la 0)"""