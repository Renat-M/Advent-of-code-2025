import unittest
from task2 import task2

class TestTask2(unittest.TestCase):
    def test_task2(self):
        result = task2('test.txt')
        expected_result = 3121910778619
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()