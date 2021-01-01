# test_mock_first.py
import unittest
from unittest import mock

from mock_first import MockFirst

secrets = {
    'hello': 'superSecretValue'
}


@mock.patch('mock_first.secrets_config', secrets)
class TestMockFirst(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mockfirst = MockFirst()

    def test_variable_setup(self):
        self.assertEqual(self.mockfirst.secrets_config, secrets)
