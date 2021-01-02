# test_mock_first.py
import unittest
from unittest import mock

from mock_first import MyMockFileFirst, MySecondMockFile

secrets = {
    'DEFAULT': {
        'secretkey': 'mockedSecretValue',
    }
}


@mock.patch('mock_first.secrets_config', secrets)
class TestMockFirst(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.myclass = MyMockFileFirst()

    def test_variable_setup(self):
        self.assertEqual(
            self.myclass.do_something_with_secrets_value(),
            'mockedSecretValuehello'
        )
        self.assertNotEqual(
            self.myclass.do_something_with_secrets_value(),
            'superSecretValuehello'
        )


@mock.patch('mock_first.secrets_config', secrets)
class TestMySecondMockFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.myclass = MySecondMockFile()

    def test_second_variable_setup(self):
        self.assertEqual(
            self.myclass.do_something_with_secrets_value(),
            'mockedSecretValuehello'
        )
        self.assertNotEqual(
            self.myclass.do_something_with_secrets_value(),
            'superSecretValuehello'
        )


if __name__ == '__main__':
    unittest.main()
