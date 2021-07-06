from mycalc import MyCalc
import unittest
from unittest.mock import Mock
from unittest.mock import patch

class TestMyCalc(unittest.TestCase):
    def setUp(self):
        self.mycalc1_0 = MyCalc(1, 0)
        self.mycalc36_12 = MyCalc(36, 12)

    def test_add(self):
        self.assertEqual(self.mycalc1_0.add(), 1)
        self.assertEqual(self.mycalc36_12.add(), 40)

    def test_mod_divide(self):
        self.assertRaises(ValueError, self.mycalc1_0.mod_divide)

    def test_rand_between(self):
        with patch('mycalc.random.random') as fake_random:
            fake_random.return_value = .5
        
            rb = self.mycalc1_0.rand_between()
            self.assertEqual(rb, 0.5)
        

if __name__ == '__main__':
    unittest.main()
