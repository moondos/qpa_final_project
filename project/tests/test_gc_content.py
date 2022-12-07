import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import unittest
from script import gc_content_subseq

'''
This is a script for testing the functions of script.py built in Part 1 and
Part3 of qpa final project. Testing is done using unittest module.
'''


class testGcContent(unittest.TestCase):

    def test_gc_content_subseq(self):
        '''This is a test for GC content function input raising exception for wrong type'''
        self.assertRaises(Exception, gc_content_subseq, 12, 3)


if __name__ == '__main__':
    unittest.main()
