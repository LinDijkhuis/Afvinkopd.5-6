class students:

    def __init__(self, voornaam):
        self.__voornaam = voornaam
        self.__vooropleiding = ""
        self.setvoornaam(voornaam)

    def setvoornaam(self, naam):
        self.__naam = naam

    def getvoornaam(self):
        return self.__naam

    def setleeftijd(self, leeftijd):
        self.__leeftijd = leeftijd

    def getleeftijd(self):
        return self.__leeftijd


def main():
    naam = voornaam("Lin")
    print(naam.getvoornaam(), hans.getvooropleiding())

    # voornaam1 = students()
    # voornaam2 = students()
    # voornaam3 = students()
    # voornaam4 = students()
    # voornaam1.setvoornaam("Lin")
    # voornaam2.setvoornaam("Macha")
    # voornaam3.setvoornaam("Esmay")
    # voornaam4.setvoornaam("Henk")
    # # Controleren of het private is.
    # # print(voornaam4)
    # print(voornaam1.getvoornaam())
    # print(voornaam2.getvoornaam())
    # print(voornaam3.getvoornaam())
    # print(voornaam4.getvoornaam())
    # voornaam1.setleeftijd("18")
    # print(voornaam1.getleeftijd())

main()




# if header.startswith(">"):
#     self.__header = header
# else:
#     print("header is geen header")
