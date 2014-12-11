''' PYLINT, PEP '''

foo = long_function_name(var_one, var_two,
                         var_three, var_four)
 
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
 
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


foo = long_function_name(var_one, var_two,
    var_three, var_four)
    
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
    


''' TESTY JEDNOSTKOWE '''

import unittest

class MathTest(unittest.TestCase):
    def test_add(self):
    self.assertEqual(2 + 3, 5)
    def test_sub(self):
    self.assertEqual(5 - 3, 2)
    
if __name__ == '__main__':
    unittest.main()
    
python python/tests/test.py
    
# Asercje w testach

self.assertEqual(2 + 3, 5)
self.assertAlmostEqual(0.1 + 0.2, 0.3, delta=1e-6)
self.assertNotEqual('żółw', u'Żółw')
self.assertTrue([0])
self.assertFalse([])
x = []
y = x
self.assertIs(x, y)
self.assertIn('x', ['x'])
self.assertIsInstance([], list)
self.assertIsNone(None)
self.assertItemsEqual((2, 3), [2, 3])


# Code coverage

sudo pip install coverage
coverage run python/hello.py
coverage report -m
coverage html