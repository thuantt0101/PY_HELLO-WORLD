# test_simple_unittest.py
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('python'.upper(), 'PYTHON')

    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        # self.assertFalse('Python'.isupper())

    
    def test_islower(self):
        # self.assertTrue('PYTHON'.islower())
        self.assertFalse('Python'.islower())

    def test_split(self):
        test_string = 'Python is a best language'
        self.assertEqual(test_string.split(), ['Python', 'is', 'a', 'best', 'language'])

        # check that test_string.split fails when the seperator is not  a string
        with self.assertRaises(TypeError):
            test_string.split(2)

print(__name__)
if __name__ == '__main__':

    # unittest.main(verbosity=2)
    # Để khởi chạy các test case trong một module, cần đặt gọi đến unittest.main() 
    # của module đó. unittest.main() thường đặt ở cuối cùng của module (file code).
    # or you can call specific like this :python -m unittest test_simple_unittest    
    unittest.main(verbosity=2)