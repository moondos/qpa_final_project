from data.retrieving import get_rna_bases, get_proteins

import matplotlib.pyplot as plt
from Bio import SeqIO

'''
This script consists of two functions for translation DNA into RNA and RNA
into protein sequence
'''

'''Getting DNA <-> RNA Map from PostgreSQL database'''
rna_map = get_rna_bases()
'''Getting RNA <-> Protein Map from PostgreSQL database'''
protein_map = get_proteins()


def convert_dna_to_rna(sequence: str) -> str:
    '''A function converting DNA sequence to RNA'''
    # rna = sequence.replace("T", "U") # code for the first task
    rna = ""
    for i in sequence:
        rna += rna_map[i]
    return rna


def convert_rna_to_dna(sequence: str) -> str:
    '''A function converting RNA sequence to DNA. Not used in this stage'''
    dna = sequence.replace("U", "T")
    return dna


def convert_rna_to_protein(sequence: str) -> str:
    '''A function converting RNA sequence to Protein'''
    s_len = len(sequence)
    temp = 0        # temp varibale for codon triplet iteration
    triplet = 3     # number of codons for one polypeptide
    protein = ""
    for i in list(range(triplet, s_len+1, triplet)):
        codon = protein_map[sequence[temp:i]]
        protein += codon
        temp = i
    return protein


# Test case
dna = "ATTTGGCTACTAACAATCTA"
# rna = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
#  DOCKER TEST
# print("Enter DNA sequence:")
# dna = input()  # User input
rna = convert_dna_to_rna(dna)
protein = convert_rna_to_protein(rna)
print(protein)


'''
Task 3 of the project, plotting GC-content of genom
'''


def gc_content(seq: str) -> int:
    '''GC content in DNA/RNA sequence'''
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)


def gc_content_subseq(seq: str, k=200) -> list:
    '''GC content in DNA/RNA sub-sequence length k'''
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


covid_genom = SeqIO.read("data/genomic.fna", "fasta")

# print(len(covid_genom.seq))

seq = list(covid_genom)

gc_content_lst = gc_content_subseq(seq, 100)
# print(gc_content_lst)

plt.plot(gc_content_lst)
plt.title("GC-content distribution")
plt.xlabel("Genome position")
plt.ylabel("GC-content(%)")
# plt.show()
plt.savefig("image/gc_dist.png")
