"""
Auteur: Lin Dijkhuis
Datum: 14 december 2021
"""

import re


class DNA:

    def __init__(self):
        self.__dna = open_file("Felis_catus.Felis_catus_8.0.cdna.all.fa")

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


def open_file(file):
    open_file = open(file, "r")
    fasta_bestand = []
    inhoud = open_file.read()
    splits = re.split(">", inhoud, re.MULTILINE)
    del splits[0]
    for line in splits:
        header_seq = []
        header, sequentie = line.split("\n", 1)
        header_seq.append(header)
        sequentie = sequentie.replace("\n", "")
        header_seq.append(sequentie)
        fasta_bestand.append(header_seq)

    return fasta_bestand


if __name__ == '__main__':
    # fasta_bestand = open_file("Felis_catus.Felis_catus_8.0.cdna.all.fa")
    # data string dna, zit in object dna_seq.
    dna_seq = DNA()
    if dna_seq.get__dna() != "":
        print("DNA sequentie: ", dna_seq.get__dna())
        print("RNA sequentie: ", dna_seq.get__transcript())
        print("Lengte sequentie: ", dna_seq.get__length())
        print("GC%: ", dna_seq.gc__percentage())
