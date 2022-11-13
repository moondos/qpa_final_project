from models import Base, Session, engine, DNA,RNA, Codon, Polypeptide

def recreate_database():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

recreate_database()

rna_a = RNA(rna_base="A")
rna_c = RNA(rna_base="C")
rna_g = RNA(rna_base="G")
rna_u = RNA(rna_base="U")

dna_a = DNA(dna_base="A", rna_base=rna_a)
dna_c = DNA(dna_base="C", rna_base=rna_c)
dna_g = DNA(dna_base="G", rna_base=rna_g)
dna_t = DNA(dna_base="T", rna_base=rna_u)

dna_bases = [dna_a, dna_c, dna_g, dna_t]

new_map = {'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Y': ['UAU', 'UAC'], 
        '.': ['UAA', 'UAG', 'UGA'], 'C': ['UGU', 'UGC'], 'W': ['UGG'], 
        'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'], 
        'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 
        'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 
        'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 
        'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 
        'G': ['GGU', 'GGC', 'GGA', 'GGG']}

s = Session()

s.add_all(dna_bases)

for pp, codons in new_map.items():
    pp = Polypeptide(polypeptide = pp)
    for codon in codons:
        codon = Codon(codon = codon, polypeptide = pp)
        s.add(codon)
    # print(codon, "->" , pp)

s.commit()
s.close()