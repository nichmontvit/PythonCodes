# you can use functions from other files by using the from import keyword: from [insert the name of the script containing the 
# function ] import [insert here the name of the function you wish to use]

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_emptystring(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_double_name(self):
        testcase = "Hopper, Grace N."
        expected = "Grace N. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()
