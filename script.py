from data.retrieving import *

# This script consists of two functions for translation DNA into RNA and RNA into protein sequence

rna_map = get_rna_bases()       # Getting DNA <-> RNA Map from PostgreSQL database
protein_map = get_proteins()    # Getting RNA <-> Protein Map from PostgreSQL database


def convert_dna_to_rna(sequence) -> str:
    # A function converting DNA sequence to RNA
    # rna = sequence.replace("T", "U") # code for the first task
    rna = ""
    for i in sequence:
        rna += rna_map[i]
    return rna

def convert_rna_to_dna(sequence) -> str:
    # A function converting RNA sequence to DNA
    # Not used in this stage
    dna = sequence.replace("U", "T")
    return dna

def convert_rna_to_protein(sequence) -> str:
    # A function converting RNA sequence to Protein
    s_len = len(sequence)
    index_lst = list(range(3,s_len+1,3))
    temp = 0
    protein = ""
    for i in index_lst:
        codon = protein_map[sequence[temp:i]]
        protein += codon
        temp = i
    return protein

# Test case
# dna = "ATTTGGCTACTAACAATCTA"
# rna = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
print("Enter DNA sequence:")
dna = input() # User input 
rna = convert_dna_to_rna(dna)
protein = convert_rna_to_protein(rna)
print(protein)
