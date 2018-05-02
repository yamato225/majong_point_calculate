import unittest
from MajongPointCalculate import MajongPointCalculate

class TestMajongPointCalculate(unittest.TestCase):
    def test_setvaluecheck_errorcase(self):
        mytile = [1,2,3,4]
        mytsumo = 2
        with self.assertRaises(ValueError):
            MajongPointCalculate(mytile,mytsumo)

    def test_setvaluecheck_normal(self):
        mytile = [1,2,3,4,5,6,7,8,9,11,12,13,14]
        mytsumo = 2
        mycalc = MajongPointCalculate(mytile,mytsumo)
        self.assertEqual(mycalc.getTiles(),{
            'tiles':[1,2,3,4,5,6,7,8,9,11,12,13,14],
            'tsumo': 2
            })
    
    def test_isKokushi1(self):
        mytile = [31,31,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 32
        mycalc = MajongPointCalculate(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),True)

    def test_isKokushi2(self):
        mytile = [31,32,33,34,41,42,43,1,9,11,19,22,29]
        mytsumo = 31
        mycalc = MajongPointCalculate(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),False)

    def test_isKokushi3(self):
        mytile = [31,31,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 32
        mycalc = MajongPointCalculate(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),True)
    

if __name__ == '__main__':
    unittest.main()