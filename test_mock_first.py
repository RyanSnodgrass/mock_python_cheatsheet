# test_mock_first.py
import unittest
from unittest import mock

from mock_first import MyMockFileFirst

secrets = {
    'DEFAULT': {
        'secretkey': 'mockedSecretValues',
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
            'mockedSecretValueshello'
        )
        self.assertNotEqual(
            self.myclass.do_something_with_secrets_value(),
            'superSecretValuehello'
        )


if __name__ == '__main__':
    unittest.main()
