import unittest
from Operations.create_account import *


class TestCreateAccount(unittest.TestCase):

    def testPass(self):
        self.assertTrue(change_status(True), msg='Prueba no pasa porque la entrada es distinta a True')
        self.assertFalse(change_status(False), msg='Prueba no pasa porque la entrada es distinta a False')

    def testFail(self):
        self.assertNotEqual(change_status(2), None)
        self.assertEqual(change_status(None), None)
        self.assertNotEqual(change_status('Hola'), None)


if __name__ == '__main__':
    unittest.main()
