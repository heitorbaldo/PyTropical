'''
unittest / numpy.testing
'''

import unittest
from unittest import TestCase
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from pytropical.tropical_algebra import MaxPlusAlgebra, MinPlusAlgebra


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

maxp = MaxPlusAlgebra()
minp = MinPlusAlgebra()
inf = maxp.inf

v1 = [1, 0, -93]
v2 = [1, 2, -90]
a = 3

max_vec_trop_sum_1 = [1, 2, -90]
max_vec_trop_scalar_mult_1 = [4, 3, -90]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


class TestMaxTropOp(TestCase):
    
    def test_trop_sum(self):
        self.assertEqual(maxp.trop_sum(2, 6), 6)
        self.assertEqual(maxp.trop_sum(0, 6), 6)
        self.assertEqual(maxp.trop_sum(20, -9), 20)
        
    def test_trop_mult(self):
        self.assertEqual(maxp.trop_mult(2, 6), 8)
        self.assertEqual(maxp.trop_mult(0, 6), 6)
        self.assertEqual(maxp.trop_mult(20, -9), 11)
        
    def test_trop_pow(self):
        self.assertEqual(maxp.trop_pow(2, 3), 6)
        self.assertEqual(maxp.trop_pow(3, 4), 12)
        self.assertEqual(maxp.trop_pow(10, 5), 50)
        self.assertEqual(maxp.trop_pow(10, 10), 100)
        

class TestMaxVecTropOp(TestCase):
    
    @staticmethod
    def test_vec_trop_sum():
        np.testing.assert_array_equal(maxp.vec_trop_sum(v1, v2), max_vec_trop_sum_1)
        
    @staticmethod
    def test_vec_trop_scalar_mult():
        np.testing.assert_array_equal(maxp.vec_trop_scalar_mult(a, v1), max_vec_trop_scalar_mult_1)


class TestMinTropOp(TestCase):
    
    def test_trop_sum(self):
        self.assertEqual(minp.trop_sum(2, 6), 2)
        self.assertEqual(minp.trop_sum(0, 6), 0)
        self.assertEqual(minp.trop_sum(20, -9), -9)
        
    def test_trop_mult(self):
        self.assertEqual(minp.trop_mult(2, 6), 8)
        self.assertEqual(minp.trop_mult(0, 6), 6)
        self.assertEqual(minp.trop_mult(20, -9), 11)
        

if __name__ == '__main__':
    unittest.main()