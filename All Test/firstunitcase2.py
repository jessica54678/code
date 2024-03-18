import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("This is run before")

    def testa(self):
        print("This is test")
        self.assertEqual("actual","actual",'There is error')

    def test_a(self):
        print("This is test2")

    def tearDown(self):
        print("This is run after")
