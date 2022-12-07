import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import unittest
from script import convert_rna_to_protein

'''
This is a script for testing convert_rna_to_protein function of script.py
built in Part 1 of qpa final project. Testing is done using unittest module.
'''


class testRnaToProtein(unittest.TestCase):

    def test_convert_rna_to_protein(self):
        '''This is a test for DNA to RNA convertion'''
        self.assertEqual(convert_rna_to_protein("AUUUGGCUACUAACAAUCUA"), "IWLLTI")
        self.assertEqual(convert_rna_to_protein("GUUGUAAUGGCCUACAUUA"), "VVMAYI")
        self.assertEqual(convert_rna_to_protein("CAGGUGGUGUUGUUCAGUU"), "QVVLFS")
        self.assertEqual(convert_rna_to_protein("GCUAACUAAC"), "AN.")
        self.assertEqual(convert_rna_to_protein("GCUAACUAACAUCUUUGGCACUGUU"), "AN.HLWHC")
        self.assertEqual(convert_rna_to_protein("UAUGAAAAACUCAAA"), "YEKLK")
        self.assertEqual(convert_rna_to_protein("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"), "PVLDWLEEKF")


if __name__ == '__main__':
    unittest.main()
