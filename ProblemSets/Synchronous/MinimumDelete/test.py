import unittest
from main import MinimumDelete

class TestMinimumDelete(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.test_cases = [('aab', 0), ('aaabbbcc', 2), ('ceabaacb', 2), ('abcdefg', 6), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 0)]
        super().__init__(*args, **kwargs)
    
    def test_solution_0(self):
        for test_case in self.test_cases:
            m = MinimumDelete(test_case[0])
            self.assertEqual(test_case[1], m('_solution_0'))
    
    def test_solution_1(self):
        for test_case in self.test_cases:
            m = MinimumDelete(test_case[0])
            self.assertEqual(test_case[1], m('_solution_1'))


if __name__ == '__main__':
    unittest.main()
