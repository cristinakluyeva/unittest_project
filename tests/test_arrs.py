import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get(["do", "re", "mi"], 0, "test"), "do")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def unittest_get(self):
        self.assertTrue(arrs.my_slice([12, 13, 14, 15], -3, -1), [13, 14])

    def exclusion_test_get(self):
        with self.assertRaises(IndexError):
            (arrs.get([], 0, "test"), "test")


if __name__ == '__main__':
    unittest.main()