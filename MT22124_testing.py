

import unittest


class main(unittest.TestCase):
    def test_1(self):
        a = 'IIITD'
        b = 'IIITd'
        self.assertEqual(a, b)

    def test_bool(self):
        a = True
        b = True
        self.assertEqual(a, b)

class test():
    def __init__(self):
        unittest.main()




if __name__ == '__main__':
    test()