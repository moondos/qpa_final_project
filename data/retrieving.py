def get_rna_bases():

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

    from data.models import DNA, Codon, Session, engine

    protein_map = {}

    s = Session()

    # dna_bases = s.query(DNA).all()

    # # print(dna_bases)

    # for base in dna_bases:
    #     print(base)

    proteins = s.query(Codon).all()

    for protein in proteins:
        cp = str(protein).split(" ")
        protein_map[cp[0]] = cp[1]   

    s.close()

    return protein_map