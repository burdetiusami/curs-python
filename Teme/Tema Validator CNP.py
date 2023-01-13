while True:

    cnp = input(
        "\nc = opreste programul\n"
        "Introduceti cnp-ul: "
    )

    if cnp == "c":
        break

    if not cnp.isnumeric():
        print('Cnp-ul nu poate fi format din litere, ci doar numere')
        continue

    cnp_format = ['S', 'A', 'A', 'L', 'L', 'Z', 'Z', 'J', 'J', 'N', 'N', 'N', 'C']
    listcnp = [elem for elem in cnp]

    cnp_dict = {
        'S': cnp[0],
        'AA': cnp[1:3],
        'LL': cnp[3:5],
        'ZZ': cnp[5:7],
        'JJ': cnp[7:9],
        'NNN': cnp[9:12],
        'C': cnp[-1],
    }

    control_number = 279146358279
    listcnp = list(map(int, str(cnp)))
    control_number_list = list(map(int, str(control_number)))
    listcnp_c = listcnp[: -1]
    list_product = list(map(lambda x, y: x * y, listcnp_c, control_number_list))
    c_product = sum(list_product)
    c_product_modulus = c_product % 11

    if len(cnp) != 13:
        print("Numarul de caractere introdus trebuie sa fie 13")
    else:
        if int(cnp_dict['ZZ']) > 31:
            print("Ziua nasterii este incorecta")

        if int(cnp_dict['LL']) > 12:
            print("Luna nasterii este incorecta")

        if int(cnp_dict['JJ']) > 52:
            print("Codul Judetului este incorect")

        if c_product % 11 == c_product_modulus:
            if c_product_modulus != int(cnp_dict['C']):
                print("Cnp-ul introdus este incorect")
            else:
                print("Cnp-ul introdus este corect")

print()
