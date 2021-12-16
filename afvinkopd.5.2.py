"""
Auteur: Lin Dijkhuis
Datum: 6 december 2021
"""

import re


class DNA:

    def __init__(self, dna):
        self.__dna = ""
        self.set__dna(dna)

    def set__dna(self, dna):
        """Accepteert DNA string en retourneert niets.
        Kan enkel DNA instance maken met DNA nucleotiden (ATGC)
        of N van onbekend.
        """
        if re.search("[^ATGCN]", dna):
            print("No DNA")
        else:
            self.__dna = dna

    def get__dna(self):
        """Retourneert de DNA string.
        """
        return self.__dna

    def get__transcript(self):
        """Transcript RNA retourneert
        :return getTranscript"""
        # Van begin tot eind, omgedraaid, stapgrootte min 1.
        return self.get__dna()[::-1].replace("T", "U")

    def get__length(self):
        """Retourneert de lengte retourneert van de DNA streng.
        """
        return len(self.get__dna())

    def gc__percentage(self):
        try:
            gc = self.get__dna()
            g_per = gc.count("G")
            c_per = gc.count("C")
            gc_per = (g_per + c_per) / self.get__length() * 100
            return gc_per

        except (ZeroDivisionError):
            return None


if __name__ == '__main__':
    dna = "ATGCTACGCGNATTCTGGNCATGTCT"
    # data string dna, zit in object dna_seq.
    dna_seq = DNA(dna)
    if dna_seq.get__dna() != "":
        print("DNA sequentie: ", dna_seq.get__dna())
        print("RNA sequentie: ", dna_seq.get__transcript())
        print("Lengte sequentie: ", dna_seq.get__length())
        print("GC%: ", dna_seq.gc__percentage())
