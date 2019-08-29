import unittest
from app import clases


class TestClass(unittest.TestCase):
    def test_clases(self):
        self.assertEqual(clases(1), 9)

    def test_clases2(self):
        self.assertEqual(clases(2), 14)


if __name__ == '__main__':
     unittest.main()