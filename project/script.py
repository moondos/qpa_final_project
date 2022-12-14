from data.retrieving import get_rna_bases, get_proteins

import argparse
import matplotlib.pyplot as plt
from Bio import SeqIO

'''
This script consists of three functions:
1. Translation DNA sequence into RNA
2. RNA into protein sequence translation
3. Plotting GC-content of genom
'''

'''Getting DNA <-> RNA Map from PostgreSQL database'''
rna_map = get_rna_bases()
'''Getting RNA <-> Protein Map from PostgreSQL database'''
protein_map = get_proteins()


'''Functions'''


def convert_dna_to_rna(sequence: str) -> str:
    '''A function converting DNA sequence to RNA'''
    # rna = sequence.replace("T", "U") # code if no database used
    rna = ""
    for i in sequence:
        rna += rna_map[i]
    return rna


def convert_rna_to_dna(sequence: str) -> str:
    '''A function converting RNA sequence to DNA. Not used in this project'''
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


def gc_content(seq: str) -> int:
    '''GC content in DNA/RNA sequence'''
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)


def gc_content_subseq(seq: str, k=100) -> list:
    '''GC content in DNA/RNA sub-sequence length k'''
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


def read_genom(path):
    '''Command line arg as file in data/input folder with or without stepping value'''
    covid_genom = SeqIO.read(path, "fasta")
    seq = list(covid_genom)
    return seq


def log_protein(protein):
    '''Writing protein sequence to a txt file'''
    with open("data/output_data/protein.txt", "w") as f:
        print(protein, file=f)
    return


def graph_plot(gc_content_lst):
    '''Creating GC distribution plot and saving to a png file'''
    plt.plot(gc_content_lst)
    plt.title("GC-content distribution")
    plt.xlabel("Genome position")
    plt.ylabel("GC-content(%)")
    # plt.show()
    plt.savefig("data/output_data/gc_dist.png")
    return


def main():
    '''
    Command Line Arguments using Argparse module
    Passing a file as an input
    '''
    parser = argparse.ArgumentParser(description="Translates DNA sequence to RNA & Protein and generates GC-content plot")
    parser.add_argument('path', metavar='path', type=str, nargs='?', help='Enter input file', default="data/input/dna_sequence.fasta")
    parser.add_argument('step', metavar='step', type=int, nargs='?', help='Enter step for GC-content', default=100)
    args = parser.parse_args()
    path = args.path
    step = args.step

    seq = read_genom(path)
    gc_content_lst = gc_content_subseq(seq, step)
    rna = convert_dna_to_rna(seq)
    protein = convert_rna_to_protein(rna)
    print(protein)
    log_protein(protein)
    graph_plot(gc_content_lst)


if __name__ == "__main__":
    main()
