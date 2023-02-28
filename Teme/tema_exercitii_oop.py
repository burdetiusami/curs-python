class CatalogPrajituri:
    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        self.lista_prajituri.append(self)

    def afisare_prajituri(self, atr):
        if atr == "nume":
            lista_sortata = sorted(self.lista_prajituri, key=lambda x: x.nume)
        elif atr == "gramaj":
            lista_sortata = sorted(self.lista_prajituri, key=lambda x: x.gramaj)
        elif atr == "pret":
            lista_sortata = sorted(self.lista_prajituri, key=lambda x: x.pret)
        else:
            return "Atribut incorect!"

        for prajitura in lista_sortata:
            print(f"{prajitura.nume} , {prajitura.pret} Lei , {prajitura.gramaj} grame")


class Tort(CatalogPrajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)
        self.etajat = False
        self.glazura = "ciocolata"

    def setare_etajat(self, valoare):
        self.etajat = valoare

    def setare_glazura(self, valoare):
        self.glazura = valoare

    def afisare_atribute(self):
        print(f'Etajat: {self.etajat}')
        print(f'Glazura: {self.glazura}')


class Fursec(CatalogPrajituri):
    pass

# verificare: Creati 3 obiecte ale clasei Tort.
tort_1 = Tort("Birthday Cake", 100, 1500)
tort_2 = Tort("Tort de ciocolata", 60, 800)
tort_3 = Tort("Tort cu fructe si ciocolata", 50, 750)

# verificare: # verificare: Creati 3 obiecte ale clasei Fursec.
fursec_1 = Fursec("Fursecuri cu ciocolata", 10, 120)
fursec_2 = Fursec("Fursecuri cu unt", 8, 90)
fursec_3 = Fursec("Fursecuri cu gem", 30, 380)

# verificare: Afisati prajiturie dupa gramaj.
tort_2.afisare_prajituri("gramaj")
# verificare: Afisati prajiturie dupa pret.
tort_2.afisare_prajituri("pret")

# verificare:
# Folositi pentru un obiect de tip tort modificarea atributelor etajat in True si glazura in “cacao”,
# apoi pentru acest obiect folositi metoda de afisare a atributelor glazura si etajat.
tort_2.setare_etajat(True)
tort_2.setare_glazura("cacao")
tort_2.afisare_atribute()

# verificare: folositi metoda de setare/afisare si pentru un alt obiect de tip tort
tort_1.setare_etajat(False)
tort_1.setare_glazura('Fondant')
tort_1.afisare_atribute()

tort_3.afisare_atribute()



