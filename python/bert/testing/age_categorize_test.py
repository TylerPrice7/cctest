# for file in *.py; do python3 -m unittest "$file" -v; done
# Runs all the python files inside of /testing

import unittest
import sys
import os

sys.path.append(os.path.abspath(".."))

from age_categorize import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        """Test for 'Child'"""
        self.assertTrue(categorize_by_age(5)=="Child", "Categorize by Child")

    def test_adolescent(self):
        """Test for 'Adolescent'"""
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self):
        """Test for 'Adult'"""
        self.assertEqual(categorize_by_age(30), "Adult")
        self.assertIsNot(categorize_by_age(19), "Adolescent")

    def test_negative_age(self):
        """Test for negative age"""
        self.assertRaises(ValueError, lambda: categorize_by_age(-1))

if __name__ == "__main__":
    unittest.main(verbosity=2)