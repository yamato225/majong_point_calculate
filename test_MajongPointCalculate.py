
# -*- coding: utf-8 -*-

import unittest
from MajongPointCalculate import MajongPointCalculate
from MajongPointCalculate import MajongRoleDetection

class TestMajongPointCalculate(unittest.TestCase):
    #def test_setvaluecheck_errorcase(self):
    #ポン・カン・チーの場合増減あるからチェックしない。
    def test_setvalue_check_errorcase(self):
        mytile = [1,2,3,4,1,2,3,4,5,6,7,8,9,11,12,13,13,14,14]
        mytsumo = 2
        with self.assertRaises(ValueError):
            MajongRoleDetection(mytile,mytsumo)

    def test_setvaluecheck_normal(self):
        mytile = [1,2,3,4,5,6,7,8,9,11,12,13,14]
        mytsumo = 2
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.getTiles(),{
            'tiles':[1,2,3,4,5,6,7,8,9,11,12,13,14],
            'agari': 2
            })

    def test_setvaluecheck_normal2(self):
        mytile = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5]    #四槓子
        mytsumo = 5
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.getTiles(),{
            'tiles':[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5],
            'agari': 5
            })
    
    def test_isKokushi1(self):
        mytile = [31,31,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 32
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),True)

    def test_isKokushi2(self):
        mytile = [31,32,33,34,41,42,43,1,9,11,19,22,29]
        mytsumo = 31
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),False)

    def test_isKokushi3(self):
        mytile = [31,31,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 32
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(),True)

    def test_isKokushi4(self):
        mytile = [31,32,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 31
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(juusanmen=True),True)

    def test_isKokushi5(self):
        mytile = [32,32,33,34,41,42,43,1,9,11,19,21,29]
        mytsumo = 31
        mycalc = MajongRoleDetection(mytile,mytsumo)
        self.assertEqual(mycalc.isKokushiMusou(juusanmen=True),False)

    def test_isChitoitsu(self):
        mytile = [1,1,12,12,13,13,4,4,5,5,6,6,7]
        myagari = 7
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.isChitoitsu(),True)

    def test_isChitoitsu2(self):
        mytile = [1,1,12,12,13,13,4,4,5,5,7,7,7]
        myagari = 7
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.isChitoitsu(),False)

    def test_agari_pattern(self):
        mytile = [1,1,1,2,2,2,11,11,11,21,21,21,24]
        myagari = 24
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'shuntsu': [], 'anko': [1, 2, 11, 21], 'atama': 24}])

    def test_agari_pattern2(self):
        mytile = [1,2,3,2,2,2,11,11,11,21,21,21,24]
        myagari = 24
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'anko': [2,11, 21], 'atama': 24, 'shuntsu': [1]}])

    def test_agari_pattern3(self):
        mytile = [2,3,4,2,3,4,2,3,4,6,6,6,8]    #四暗刻
        myagari = 8
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'shuntsu': [2, 2, 2], 'anko': [6],'atama': 8},{'shuntsu': [], 'anko': [2, 3, 4, 6], 'atama': 8}])  

    def test_agari_pattern4(self):
        mytile = [2,2,3,4,13,14,15,31,31,31,7,8,9]
        myagari = 2
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'anko': [31], 'atama': 2, 'shuntsu': [2,7,13]}]) 

    def test_agari_pattern5(self):
        mytile = [2,2,2,2,3,4,11,11,11,11,12,13,9]
        myagari = 9
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'anko': [2,11], 'atama': 9, 'shuntsu': [2,11]}])
    
    def test_agari_pattern6(self):
        mytile = [2,3,4,3,4,5,4,5,6,5,6,7,18]
        myagari = 18
        mycalc = MajongRoleDetection(mytile,myagari)
        self.assertEqual(mycalc.agari_pattern(),[{'anko': [], 'atama': 18, 'shuntsu': [2,3,4,5]}])  


if __name__ == '__main__':
    unittest.main()