import unittest
import TwoSum

class TestTwoSum(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(TwoSum.bruteforce([1, 2, 3, 4], 5), [0, 3])
        self.assertEqual(TwoSum.bruteforce([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(TwoSum.bruteforce([], 3), [])

    def test_hastable_two_pass(self):
        self.assertEqual(TwoSum.hashtable_two_pass)
