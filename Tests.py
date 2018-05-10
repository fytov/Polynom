import unittest
from Polynomial import Polynomial

class Tests(unittest.TestCase):
    
    def test_error(self):
        self.assertRaises(TypeError, Polynomial,['a','b'])
        self.assertRaises(TypeError, Polynomial,[])
        self.assertRaises(TypeError, Polynomial.__eq__,Polynomial([1,2]),"x")
        self.assertRaises(TypeError, Polynomial,['a',4])
        self.assertRaises(TypeError, Polynomial.__add__,Polynomial([1,2]),"x")
        self.assertRaises(TypeError, Polynomial.__mul__,Polynomial([1,2]),"x")

    def test_add_pos(self):
        p = Polynomial([1,4,6,9]) 
        s = Polynomial([1,4,6]) 
        self.assertListEqual((p+s).coeffs, [1,5,10,15])
        self.assertListEqual((s+p).coeffs, [1,5,10,15])

    def test_neg_add_pos(self):
        p = Polynomial([-1,4,-6,9]) 
        s = Polynomial([1,4,6]) 
        self.assertListEqual((p+s).coeffs, [-1,5,-2,15])
        self.assertListEqual((s+p).coeffs, [-1,5,-2,15])

    def test_neg_add_pos_c(self):
        p = Polynomial([-1,4,-6,9]) 
        self.assertListEqual((p+6).coeffs, [-1,4,-6,15])
        self.assertListEqual((p-18).coeffs, [-1,4,-6,-9])

    def  test_neg_add_pos_null(self):
        p = Polynomial([0,0,0,-1,0,4,0,-6,9]) 
        s = Polynomial([0,0,0,0,0,1,4]) 
        self.assertListEqual((p+s).coeffs, [-1,0,4,0,-5,13])
        self.assertListEqual((s+p).coeffs, [-1,0,4,0,-5,13])

    def test_add_zero(self):
        p = Polynomial([0,0,0,-1,0,4,0,-6,9]) 
        s = Polynomial([0,0,0]) 
        self.assertListEqual((p+s).coeffs, [-1,0,4,0,-6,9])

    def test_add_int_c(self):
        p = Polynomial([0,0,0,-1,0,4,0,-6,9]) 
        s = 5
        self.assertListEqual((p+s).coeffs, [-1,0,4,0,-6,14])

    def test_add_int_c_left(self):
        p = Polynomial([0,0,0,-1,0,4,0,-6,9]) 
        s = 5
        self.assertListEqual((s+p).coeffs, [-1,0,4,0,-6,14])

    def test_add_float_c(self):
        p = Polynomial([0,0,0,-1,0,4,0,-6,9]) 
        s = 5.6
        self.assertListEqual((p+s).coeffs, [-1,0,4,0,-6,14.6])

    def test_add_float(self):
        p = Polynomial([0.,0,0.,-1,0,4.5,0,-6,9.9]) 
        s = Polynomial([0,0,0,0,0,1,4]) 
        self.assertListEqual((p+s).coeffs, [-1,0,4.5,0,-5,13.9])
        self.assertListEqual((s+p).coeffs, [-1,0,4.5,0,-5,13.9])    

    def test_sub(self):
        p = Polynomial([0.,0,0.,-1,0,4.5,0,-6,9.9]) 
        s = Polynomial([0,0,0,0,0,1,4]) 
        self.assertListEqual((p-s).coeffs, [-1,0,4.5,0,-7,5.9])
        self.assertListEqual((s-p).coeffs, [1,0,-4.5,0,7,-5.9])

    def test_mult(self):
        p = Polynomial([0.,0,0.,-1,0,4.5,0,-6,9.9]) 
        s = Polynomial([0,0,0,0,0,1,4]) 
        self.assertListEqual((p*s).coeffs, (s*p).coeffs)
        p = Polynomial([1, -1, 1]) 
        s = Polynomial([-1, 1])  
        self.assertEqual((p*s).coeffs, [-1, 2, -2, 1]) 

    def test_mult_zero(self):
        p = Polynomial([1, -1, 1]) 
        s = Polynomial([0, 0])  
        self.assertEqual((p*s).coeffs, [0]) 

    def test_mult_float(self):
        p = Polynomial([1.5, -1.2, 1.0]) 
        s = Polynomial([-1, 1])  
        self.assertEqual((p*s).coeffs, [-1.5, 2.7, -2.2, 1]) 

    def test_mult_float_c(self):
        p = Polynomial([1.5, -1.2, 1.0]) 
        s = 5
        self.assertEqual((p*s).coeffs, [7.5, -6, 5]) 

    def test_mult_c(self):
        p = Polynomial([5, -1, 1]) 
        s = 5
        self.assertEqual((s*p).coeffs, [25, -5, 5])

    def test_mult_c_left(self):
        p = Polynomial([5, -1, 1]) 
        s = 5
        self.assertEqual((p*s).coeffs, [25, -5, 5])

    def test_str(self):
        p = Polynomial([-1,-6,0]) 
        self.assertEqual(str(p), "-x2-6x")
        p = Polynomial([-1,-4,-6]) 
        self.assertEqual(str(p), "-x2-4x-6")
        p = Polynomial([0]) 
        self.assertEqual(str(p), "0")
        p = Polynomial([0,0,0]) 
        self.assertEqual(str(p), "0")
        p = Polynomial([1,4,80]) 
        self.assertEqual(str(p), "x2+4x+80")
        p = Polynomial([1,0,6]) 
        self.assertEqual(str(p), "x2+6")
        p = Polynomial([-1,4,-16]) 
        self.assertEqual(str(p), "-x2+4x-16")
        
    def test_str_float(self):
        p = Polynomial([0.0]) 
        self.assertEqual(str(p), "0")
        p = Polynomial([0.0,0.0,0.0]) 
        self.assertEqual(str(p), "0")
        p = Polynomial([-1.2,4.5,-6.8]) 
        self.assertEqual(str(p), "-1.2x2+4.5x-6.8")
        p = Polynomial([-1.2,0.0,-6.8]) 
        self.assertEqual(str(p), "-1.2x2-6.8")

    def test_eq(self):
        p = Polynomial([1,4,6]) 
        s = Polynomial([0,0,0,0,0,1,4]) 
        self.assertEqual(p, Polynomial([1,4,6]))
        self.assertTrue(p == Polynomial([1,4,6]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)
        s = Polynomial([0,0,0,0,0]) 
        p = 0
        self.assertTrue(p == s)
        p = "a"
        self.assertRaises(TypeError,s.__eq__,p)

    def test_eq_float(self):
        p = Polynomial([1.5,4,6.7]) 
        s = Polynomial([0,0,0,0,0,1,4.8]) 
        self.assertEqual(p, Polynomial([1.5,4,6.7]))
        self.assertTrue(p == Polynomial([1.5,4,6.7]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)

if __name__ == '__main__':
    unittest.main()