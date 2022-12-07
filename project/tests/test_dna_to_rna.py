import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import unittest
from script import convert_dna_to_rna

'''
This is a script for testing convert_dna_to_rna function of script.py built in
Part 1 of qpa final project. Testing is done using unittest module.
'''


class testDnaToRna(unittest.TestCase):

    def test_convert_dna_to_rna(self):
        '''This is a test for DNA to RNA convertion'''
        self.assertEqual(convert_dna_to_rna("ATTTGGCTACTAACAATCTA"), "AUUUGGCUACUAACAAUCUA")
        self.assertEqual(convert_dna_to_rna("GTTGTAATGGCCTACATTA"), "GUUGUAAUGGCCUACAUUA")
        self.assertEqual(convert_dna_to_rna("CAGGTGGTGTTGTTCAGTT"), "CAGGUGGUGUUGUUCAGUU")
        self.assertEqual(convert_dna_to_rna("GCTAACTAAC"), "GCUAACUAAC")
        self.assertEqual(convert_dna_to_rna("GCTAACTAACATCTTTGGCACTGTT"), "GCUAACUAACAUCUUUGGCACUGUU")
        self.assertEqual(convert_dna_to_rna("TATGAAAAACTCAAA"), "UAUGAAAAACUCAAA")
        self.assertEqual(convert_dna_to_rna("CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"), "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU")


if __name__ == '__main__':
    unittest.main()
