import unittest
from func import cps7921

class TestSampleMethods(unittest.TestCase):

    def test_cps7921(self):
      self.assertEqual(cps7921(7), 70)

if __name__ == '__main__':
    unittest.main()
