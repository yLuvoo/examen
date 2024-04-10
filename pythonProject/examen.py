# 1 sarcina
class Canine:
    def __init__(self, specie, an):
        self.specie = specie
        self.an = an
    def display_Stats(self):
        print(f"A fost adaugat {self.specie} cu varsta de {self.an}")

class Caine(Canine):
    def __init__(self, specie, an, rasa):
        super().__init__(specie, an)
        self.rasa = rasa

    def sunet(self):
        print("Sunetul care il face animalul tau este: Ham-ham")

Caine = Caine(specie = Canine, an = 3, rasa = "Dalmatian" )
print(Caine.display_Stats())
print(Caine.sunet())

# 4 sarcina
class Clasa_9:
    def __init__(self):
        self.elev = {}

    def adaugarea_elev(self, **kwargs):
        for nume, varsta in kwargs.items():
            self.elev[nume] = varsta

    def Display_elev(self):
        print("Elevii din clasa 9:")
        for nume, varsta in self.elev.items():
            print(f"Numele: {nume}, Varsta de {varsta}")

clasa = Clasa_9()
clasa.adaugarea_elev(Mihai=14, Maria=15, Marian=16)
clasa.Display_elev()