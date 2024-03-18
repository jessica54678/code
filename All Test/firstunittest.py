import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is run before")

    def testa(self):
        print("This is test")
        self.assertEqual("actual","actual",'There is error')

    def test_a(self):
        print("This is test2")

    @classmethod
    def tearDownClass(cls):
        print("This is run after")
