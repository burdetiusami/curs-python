
# 1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
# caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
# preluat automat de la tastatura.

user_name = input("Introduceti-va numele: ")
character_input = input("Introduceti un sir de caractere: ")

if str(character_input).isdigit():
    print("Sirul acesta este un sir de numere")
elif character_input.isalpha():
    print("Sirul de caractere a fost gasit de " + user_name)
else:
    print("Sirul de caractere nu este nici un string si nici un sir de numere")


# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

num_inpt = int(input("Introduceti un numar intreg: "))

if (num_inpt % 2) == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")


# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest)

year_input = int(input("Introduceti anul: "))

if (year_input % 4) == 0 and ((year_input % 400) == 0 or (year_input % 100) != 0):
    print("Anul este bisect")
else:
    print("Anul nu este bisect")


# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

user_num = int(input("Introduceti un numar: "))

if 0 < user_num < 10:
    print("Numarul este pozitiv si mai mic decat 10")
elif user_num == 0:
    print("Numarul este 0")
elif user_num < 0:
    print(user_num * -1)
else:
    print("Numarul este pozitiv dar mai mare sau egal ca 10")


# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
#
# “”” 1 – Afisare lista de cumparaturi
#
# 2 – Adaugare element
#
# 3 – Stergere element
#
# 4 – Sterere lista de cumparaturi
#
# 5 - Cautare in lista de cumparaturi “””
#
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”


"""
1 – Afisare lista de cumparaturi

2 – Adaugare element

3 – Stergere element

4 – Sterere lista de cumparaturi

5 - Cautare in lista de cumparaturi 
"""

menu_nr = int(input("Introduceti un numar de la 1 la 5: "))

if menu_nr == 1:
    print("Afisare lista de cumparaturi")
elif menu_nr == 2:
    print("Adaugare element")
elif menu_nr == 3:
    print("Stergere element")
elif menu_nr == 4:
    print("Sterere lista de cumparaturi")
elif menu_nr == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")
