from letters import LetterCompiler
import unittest

class TestCompiler(unittest.TestCase): 
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE

unittest.main()

# use this command to make the code run in the jupyter notebook
# unittest.main(argv = ['first-arg-is-ignored'], exit = False)
    