import unittest
import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test_case_1(self):
        contrived_func.contrived_func(1)

    def test_case_2(self):
        contrived_func.contrived_func(2)

    def test_case_3(self):
        contrived_func.contrived_func(0)


if __name__ == '__main__':
    unittest.main()