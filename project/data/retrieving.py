from data.models import DNA, Codon
from data.crud import Session

'''
Script for retrieving tables info to Python dictionaries for
convenient usage in the script.py
'''


def get_rna_bases() -> dict:
    '''Retriving RNA to DNA map'''

    rna_map = {}

    session = Session()
    dna_bases = session.query(DNA).all()

    for base in dna_bases:
        cp = str(base).split(" ")
        rna_map[cp[0]] = cp[1]

    session.close()

    return rna_map


def get_proteins() -> dict:
    '''Retriving Polypeptide to Codon map'''

    protein_map = {}

    session = Session()
    proteins = session.query(Codon).all()

    for protein in proteins:
        codon_pp = str(protein).split(" ")
        protein_map[codon_pp[0]] = codon_pp[1]

    session.close()

    return protein_map
