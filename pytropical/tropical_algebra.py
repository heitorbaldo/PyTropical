"""
Tropical Algebra (Min-Plus/Max-Plus Algebras).
"""

import math
import numpy as np


__all__ = [
    "MaxPlusAlgebra",
    "MinPlusAlgebra",
]


class MaxPlusAlgebra:
    
    def __init__(self):
        self.inf = -np.Inf
    
    
    def trop_sum(self, a, b, symbol=False):
        '''Returns the tropical sum (maximum) of a and b.
        Parameters
        ----------
        a, b: (float) real numbers.
        '''
        if symbol == False:
            return max(a, b)
        else:
            print(str(a)+'⨁'+str(b)+' =', max(a, b))

            
    def trop_mult(self, a, b, symbol=False):
        '''Returns the tropical multiplication (sum) of a and b.
        Parameters
        ----------
        a, b: (float) real numbers.
        '''
        if symbol == False:
            return a+b
        else:
            print(str(a)+'⨀'+str(b)+' =', a+b)
       
    
    def trop_pow(self, a, n):
        '''Returns tropical exponentiation of a.
        Parameters
        ----------
        a: (float) a real number.
        n: (integer) the power.
        '''
        v = [a]*n
        trop_pow = sum(v) #tropical exponentiation
        return trop_pow
    
    
    def trop_polynomial(self, A):
        '''Returns the tropical polynomial of A.
        Parameters
        ----------
        A: (array) an array of coeffients and powers.
        '''
        Pol = ''
        for i in range(len(A)):
            p = str(A[i][0])+'⨀'+'x^'+str(A[i][1])
            if i < len(A)-1:
                p = p+' ⨁ '
            Pol = Pol + p
        return Pol

            
    def vec_trop_sum(self, v, w):
        '''Returns the tropical sum of two vectors v and w.
        v, w: (array) vectors of real numbers.
        '''
        V = []
        for i in range(len(v)):
            V.append(self.trop_sum(v[i], w[i]))
        return V

    
    def vec_trop_scalar_mult(self, a, v):
        '''Returns the tropical scalar multiplication of a vector v by a real number a.
        v, w: (array) vectors of real numbers.
        '''
        V = []
        for i in range(len(v)):
            V.append(self.trop_mult(a, v[i]))
        return V
    
    
    def matrix_trop_sum(self, A, B):
        '''Returns the tropical sum (maximum) of two matrices A and B.
        A, B: (array) matrices of real numbers.
        '''
        num_rows, num_cols = A.shape
        M = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                 M[i, j] = self.trop_sum(A[i, j], B[i, j])
        return M
    
    
    def matrix_trop_scalar_mult(self, a, A):
        '''Returns the tropical scalar multiplication of a matrix A by a real number a.
        A, B: (array) matrices of real numbers.
        '''
        num_rows, num_cols = A.shape
        M = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                 M[i, j] = self.trop_mult(a, A[i, j])
        return M
    
    
    def matrix_trop_mult(self, A, B):
        '''Returns the tropical multiplication of two matrices A and B.
        A, B: (array) matrices of real numbers.
        '''
        A_num_rows, A_num_cols = A.shape
        B_num_rows, B_num_cols = B.shape

        if A_num_cols != B_num_rows:
            raise ValueError("A_num_cols must be equal to B_num_rows.")

        M = np.zeros((A_num_rows, B_num_cols))

        for i in range(A_num_rows):
            for k in range(B_num_cols):
                Mult = []
                for j in range(B_num_rows):
                    Mult.append(A[i, j] + B[j, k])
                M[i, k] = max(Mult)   
        return M

    

class MinPlusAlgebra:
    
    def __init__(self):
        self.inf = np.Inf
    
    
    def trop_sum(self, a, b, symbol=False):
        '''Returns the tropical sum (minimum) of a and b.
        Parameters
        ----------
        a, b: (float) real numbers.
        '''
        if symbol == False:
            return min(a, b)
        else:
            print(str(a)+'⨁'+str(b)+' =', min(a, b))

            
    def trop_mult(self, a, b, symbol=False):
        '''Returns the tropical multiplication (sum) of a and b.
        Parameters
        ----------
        a, b: (float) real numbers.
        '''
        if symbol == False:
            return a+b
        else:
            print(str(a)+'⨀'+str(b)+' =', a+b)
    
    
    def trop_pow(self, a, n):
        '''Returns tropical exponentiation of a.
        Parameters
        ----------
        a: (float) a real number.
        n: (integer) the power.
        '''
        v = [a]*n
        trop_pow = sum(v) #tropical exponentiation
        return trop_pow
    
    
    def trop_polynomial(self, A):
        '''Returns the tropical polynomial of A.
        Parameters
        ----------
        A: (array) an array of coeffients and powers.
        '''
        Pol = ''
        for i in range(len(A)):
            p = str(A[i][0])+'⨀'+'x^'+str(A[i][1])
            if i < len(A)-1:
                p = p+' ⨁ '
            Pol = Pol + p
        return Pol

    
    def vec_trop_sum(self, v, w):
        '''Returns the tropical sum of two vectors v and w.
        v, w: (array) vectors of real numbers.
        '''
        V = []
        for i in range(len(v)):
            V.append(self.trop_sum(v[i], w[i]))
        return V

    
    def vec_trop_scalar_mult(self, a, v):
        '''Returns the tropical scalar multiplication of a vector v by a real number a.
        v, w: (array) vectors of real numbers.
        '''
        V = []
        for i in range(len(v)):
            V.append(self.trop_mult(a, v[i]))
        return V
    
     
    def matrix_trop_sum(self, A, B):
        '''Returns the tropical sum (minimum) of two matrices A and B.
        A, B: (array) matrices of real numbers.
        '''
        num_rows, num_cols = A.shape
        M = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                 M[i, j] = self.trop_sum(A[i, j], B[i, j])
        return M
    
    
    def matrix_trop_scalar_mult(self, a, A):
        '''Returns the tropical scalar multiplication of a matrix A by a real number a.
        A, B: (array) matrices of real numbers.
        '''
        num_rows, num_cols = A.shape
        M = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                 M[i, j] = self.trop_mult(a, A[i, j])
        return M
    
    
    def matrix_trop_mult(self, A, B):
        '''Returns the tropical multiplication of two matrices A and B.
        A, B: (array) matrices of real numbers.
        '''
        A_num_rows, A_num_cols = A.shape
        B_num_rows, B_num_cols = B.shape

        if A_num_cols != B_num_rows:
            raise ValueError("A_num_cols must be equal to B_num_rows.")

        M = np.zeros((A_num_rows, B_num_cols))

        for i in range(A_num_rows):
            for k in range(B_num_cols):
                Mult = []
                for j in range(B_num_rows):
                    Mult.append(A[i, j] + B[j, k])
                M[i, k] = min(Mult)   
        return M

