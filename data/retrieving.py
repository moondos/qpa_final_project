# Script for retrieving tables info to Python dictionaries for convenient usage in the script.py

def get_rna_bases():
    # Retriving RNA to DNA map
    from data.models import DNA, Codon, Session, engine

    rna_map = {}

    s = Session()
    dna_bases = s.query(DNA).all()

    for base in dna_bases:
        cp = str(base).split(" ")
        rna_map[cp[0]] = cp[1]   

    s.close()

    return rna_map

def get_proteins():
    # Retriving Polypeptide to Codon map
    from data.models import DNA, Codon, Session, engine

    protein_map = {}

    s = Session()
    proteins = s.query(Codon).all()

    for protein in proteins:
        cp = str(protein).split(" ")
        protein_map[cp[0]] = cp[1]   

    s.close()

    return protein_map