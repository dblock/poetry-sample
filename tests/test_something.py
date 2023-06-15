import unittest
from package.something import Something

class TestSomething(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Something.something(), 'something')
