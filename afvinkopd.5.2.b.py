"""
Auteur: Lin Dijkhuis
Datum: 14 december 2021
"""

import re


class DNA:

    def __init__(self, seq):
        # Bestand toegevoegd aan het object.
        # Heb init sequentie als obect gegeven.
        self.__dna = seq

    def set__dna(self, seq):
        """Accepteert DNA string en retourneert niets.
        Kan enkel DNA instance maken met DNA nucleotiden (ATGC)
        of N van onbekend.
        """
        if re.search("[^ATGCN]", seq):
            print("No DNA")
        else:
            self.__dna = seq

    def get__dna(self):
        """Retourneert de DNA string.
        """
        return self.__dna

    def get__transcript(self):
        """Transcript RNA retourneert
        :return getTranscript"""
        try:
            dna_complement_dict = {'A': 'U',
                                   'T': 'A',
                                   'G': 'C',
                                   'C': 'G'}
            complementary_strand = ''
            for dna in self.__dna:
                complementary_strand += dna_complement_dict[dna]

        except KeyError:
            print("Does not only contains, ATGCN")
        return complementary_strand
        # Van begin tot eind, omgedraaid, stapgrootte min 1.
        # return self.get__dna()#[::-1].replace("T", "U")

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


def read_fasta(file):
    """Een fasta bestand openen en lezen.
    Vervolgens het in een lijst zetten, zodat je er verder
    mee kunt werken.
    Input: fasta file
    """
    name, seq = None, []
    with open(file) as fp:
        # name is header
        # sequentie is lege lijst.
        for line in fp:
            line = line.rstrip()
            header_control = line.startswith(">", 0, 1)
            if header_control == True:
                # Yield returned een generator object inplaats van een waarde.
                # Bewaart al deze info lokaal.
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))


if __name__ == '__main__':
    # data string dna, zit in object dna_seq.
    dna_list = []
    for name, seq in read_fasta("Felis_catus.Felis_catus_8.0.cdna.all.fa"):
        # print(name, seq)

        dna_seq = DNA(seq)
        # Object aanmaken.
        dna_seq.set__dna(seq)
        # dna_list.append(dna_seq.get__dna())
        # Sequentie, data die hoort bij object.
        dna_list.append(dna_seq)
        # Object, zit alle data, sequentie en gc kun je doen.
    per_gc = []
    for i in dna_list:
        # i is object
        per_gc.append(i.gc__percentage())
    max_gc = max(per_gc)
    index_find = per_gc.index(max_gc)
    # Zoekt de index max gc% in de lijst.
    print(max_gc)
    print(index_find)
    print(dna_list[index_find].get__length())
    print(dna_list[index_find].get__transcript())


        # Voegt nu seq als data aan het object.
        # Checken of er iets te printen valt, is het niet leeg.
        # if dna_seq.get__dna() != "":
        #     print("DNA sequentie: ", dna_seq.get__dna())
        #     print("RNA sequentie: ", dna_seq.get__transcript())
        #     print("Lengte sequentie: ", dna_seq.get__length())
            # print("GC%: ", dna_seq.gc__percentage())
