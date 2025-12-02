import unittest
from task1 import task1

class TestTask1(unittest.TestCase):
    def test_task1(self):
        result = task1('test.txt')
        expected_result = 1227775554
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()