from data.retrieving import *

rna_map = get_rna_bases()
protein_map = get_proteins()


def convert_dna_to_rna(sequence) -> str:
    rna = sequence.replace("T", "U")
    return rna

def convert_rna_to_dna(sequence) -> str:
    dna = sequence.replace("U", "T")
    return dna

def convert_rna_to_protein(sequence) -> str:
    s_len = len(sequence)
    index_lst = list(range(3,s_len+1,3))
    temp = 0
    protein = ""
    for i in index_lst:
        codon = protein_map[sequence[temp:i]]
        protein += codon
        temp = i
    return protein



print("Enter DNA sequence:")
dna = input()
# rna = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
rna = convert_dna_to_rna(dna)
protein = convert_rna_to_protein(rna)
print(protein)
