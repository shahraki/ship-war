import sys
import os
sys.path.append('..')
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import import_abc
import unittest

class testmytest(unittest.TestCase):
    def test_greek(self):
        self.assertEqual(import_abc.r.geeks,"child class")

if __name__ == '__main__':
    unittest.main()