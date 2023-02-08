# import unittest
#
#
# class Testing(unittest.TestCase):
#     def test_string(self):
#         a = 'some'
#         b = 'some'
#         self.assertEqual(a, b)
#
#     def test_boolean(self):
#         a = True
#         b = True
#         self.assertEqual(a, b)
#
# if __name__ == '__main__':
#     unittest.main()


import math

def is_prime(num):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True



is_prime(3)

# is_prime(5)
#
# is_prime(12)
#
# is_prime(8)
#
# assert is_prime(7) == True