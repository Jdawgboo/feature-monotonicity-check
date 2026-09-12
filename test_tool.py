import unittest
from tool import violations
class Tests(unittest.TestCase):
 def test_order(self): self.assertEqual(violations([1,3,2,4]),[2])
if __name__=='__main__': unittest.main()
